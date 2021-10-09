from django.db import models
from django.contrib.auth.models import User


class PostManager(models.Manager):
    def getall(self):
        return self.filter.all()





class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=230)
    image = models.ImageField(upload_to="Post")
    date = models.DateTimeField(auto_now_add=True)
    

    objects = PostManager()
    
    def __str__(self):
        return str(self.user) + str(self.date)


class ProfileManager(models.Manager):
    pass

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userImage = models.ImageField(upload_to="Profiles", default ="default/defaultimg.jpg")
    bio = models.CharField(max_length=100)
    connection = models.CharField(max_length=140, blank=True)
    follower = models.IntegerField(default = 0)
    following = models.IntegerField(default = 0)
    objects = ProfileManager()
    get = ProfileManager()
    def __str__(self):
        return str(self.user)

class Public(models.Model):
    comment =models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    comm_post = models.ForeignKey(Post,on_delete=models.CASCADE,default=None)
    by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.comment) 
    

class Following(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed = models.ManyToManyField(User, related_name='followed', blank=True)
    follower = models.ManyToManyField(User, related_name='follower', blank=True)

    @classmethod
    def follow(cls,user,another_account):
        obj,create = cls.objects.get_or_create(user = user)
        obj.followed.add(another_account)
        print("followed")
    
    @classmethod
    def unfollow(cls,user,another_account):
        obj,create = cls.objects.get_or_create(user = user)
        obj.followed.remove(another_account)
        print("unfollowed")
    
    def __str__(self):
        return str(self.user)


class Like(models.Model):
    user = models.ManyToManyField(User, related_name="linkingUser")
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    
    # for liking post
    @classmethod
    def like(cls, post, liking_user):
        obj, create  = cls.objects.get_or_create(post = post)
        obj.user.add(liking_user)

    # for disliking post
    @classmethod
    def dislike(cls, post, disliking_user):
        obj, create  = cls.objects.get_or_create(post = post)
        obj.user.remove(disliking_user)

    def __str__(self):
        return str(self.post)
