from django.shortcuts import render,redirect,HttpResponse
import pyautogui as pu
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages 
from django.views.generic import TemplateView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



# Create your views here.

def home (request):
    return render( request, 'accounts/signup.html')

def signup (request): 
    
    if request.method == 'POST' :
        mail = request.POST.get('email','')
        username = request.POST.get('username','')
        name = request.POST.get('name','')
        password = request.POST.get('password','')
        conf_pass = request.POST.get('confirm_password','')
        
        userCheck = User.objects.filter(username=username) | User.objects.filter(email=mail)
        
        if userCheck:
            messages.error(request, "Username already exist")
            return redirect ('/')

        if password == conf_pass :
            if User.objects.filter (username=username).exists():
                pu.alert ("Username already exist")
            else:
                user = User.objects.create_user(first_name= name ,password = password, email= mail,username=username )
                user.save()
                pu.alert('Yikes ! ! ')
                return redirect('/user_login2')
        else: 
            pu.alert("confirm password does not match with passowrd")

    return redirect('/')

def user_login (request):
    if request.method == "POST":
        user_name = request.POST.get('username','')
        user_password = request.POST.get('password','')

        user = authenticate(username=user_name, password=user_password)
        
        if user is not None :
            login(request,user)
            messages.success(request , "Login success")
            return redirect('/Profilepage')
        else: 
            messages.error(request , "INvalid credentails")
            return redirect('/')

def user_login2(request):
    return render (request, 'loginpage.html')

def user_logout (request):
    logout(request)
    messages.success(request,'Successfully logged out ! ')
    return redirect('/')
        

class Change_Password(TemplateView):
    template_name = "accounts/password_change.html"

    def post(self,request):
        form = PasswordChangeForm(user = request.user,data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,user = request.user)
            messages.success(request, "password changed")
            return redirect("/change_password")
        else :
            for err in form.errors.values():
                messages.error(request, err)
            return redirect("/change_password")
    
    def get(self, request):
        form = PasswordChangeForm(user = request.user)
        return render(request, self.template_name,{'form': form })