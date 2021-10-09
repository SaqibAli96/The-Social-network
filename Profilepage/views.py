from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
from django.contrib import messages 
from .models import Post,Profile,Following,Like,Public
from django.contrib.auth.models import User
import pyautogui as pu 
from django.views import View
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.conf import settings 
import json
from django.core.paginator import Paginator 
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='user_login2')
def userhome (request):
    user = Following.objects.get(user = request.user)
    followed_user = [i for i in user.followed.all()]
    followed_user.append(request.user)
    posts = Post.objects.filter(user__in = followed_user).order_by("-pk")
    liked_post = [i for i in posts if Like.objects.filter(post=i,user=request.user)]
    
    data = {'posts': posts,'liked_post':  liked_post} 
        
        
    return render (request, 'Profilepage/postfeed.html',data) 


def post(request):
    if request.method == "POST":
        image_ = request.FILES['image']
        captions_ =request.POST.get('caption','')
        user_ = request.user
        post_obj = Post( user=user_,caption=captions_,image=image_)
        post_obj.save()
        messages.success(request,'Post updated')
        return redirect ('/Profilepage')
    
    else:
        messages.error(request,"It did'nt go through")
        return redirect ('/Profilepage')

def delPost (request, postId):
    post_ = Post.objects.filter(pk=postId)
    #img_path = post_[0].image.url
    post_.delete()
    messages.info(request,"POst deleted")
    return redirect ('/Profilepage')


def userProfile(request,username):
        
    if request.user.is_authenticated:    
        user = User.objects.filter(username=username)
        if user :
            user = user[0]
            profile = Profile.objects.get(user=user)
            post   = getPost(user)
            bio     = profile.bio
            conn    = profile.connection
            user_img = profile.userImage
            is_following = Following.objects.filter(user = request.user, followed = user)
            following_obj = Following.objects.get( user = user )
            follower,following = following_obj.follower.count(), following_obj.followed.count()
            
            data ={
                'user_obj':user,
                'bio':bio, 
                'conn':conn, 
                'follower':follower, 
                'following':following,
                'userImg':user_img,
                'posts': post,
                "connection" : is_following 
                }
            return render(request, 'Profilepage/userProfile.html', data)   
        
            
        else : 
            messages.info(request,"Please Login")
            return redirect("/user_login2")
    else:
        return redirect("/user_login2")

def getPost(user):
    post_obj = Post.objects.filter(user=user)
    imgList =[post_obj[i:i+3] for i in range(0, len(post_obj),3)]
    return imgList



#def comment(request):
    
@login_required(login_url='user_login2')
def commentview(request,pos_id):
    #pos_id = Post.objects.all(id)
    #print(pos_id)
    b = Public.objects.all()
    
    return render(request, 'Profilepage/comments.html',{'comments':b})

    



def follow (request, username):
    main_user = request.user 
    to_follow = User.objects.get(username=username)
    
    #check if already following 

    following = Following.objects.filter(user = main_user,followed=to_follow)
    is_following = True if following else False 

    if is_following :
        Following.unfollow(main_user,to_follow)
        is_following = False 
    else : 
        Following.follow(main_user,to_follow)
        is_following = True 
    

    resp = {
        'following' :  is_following,
    }

    response =json.dumps(resp)
    return HttpResponse(response, content_type="application/json")

@login_required(login_url='user_login2')
def about_me(request):
    return render(request,"Profilepage/about.html")





class Search_User(ListView):
    model = User
    template_name = "Profilepage/searchUser.html"
    paginate_by = 2

    def get_queryset(self):
        username = self.request.GET.get("username","")
        queryset = User.objects.filter(username__icontains = username)
        return queryset


class EditProfile(View):
    def post(self, request, *args, **kwargs):
        profile_obj = Profile.objects.get(user = request.user)
        bio = request.POST.get("Bio", "")
        img = request.FILES.get("image", "")
        if bio: profile_obj.bio = bio
        if img: profile_obj.userImage = img
        profile_obj.save()

        return HttpResponseRedirect(reverse("userprofile", args=(request.user.username,)))
# P _ { : ; p [ "

# P _ { : ; p [ "


def likePost(request):
    id = request.GET.get("likeId",'')
    post = Post.objects.get(pk=id)
    user = request.user
    like = Like.objects.filter(post=post, user=user)
    liked = False
    if like:
        Like.dislike(post,user)
    else:
        liked = True
        Like.like(post,user)    
    resp = {
        'liked': liked
    }
    response = json.dumps(resp)
    return HttpResponse(response,content_type='application.json')