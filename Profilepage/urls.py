from django.contrib import admin
from django.urls import path
from . import views
from .views import Search_User, EditProfile
urlpatterns = [
    
    path('', views.userhome, name= 'userhome'),
    path('post', views.post, name='post'),
    path('like_dislike', views.likePost, name='like_dislike_post'),
    path("<int:postId>", views.delPost, name='delPost'),
    path("<str:username>", views.userProfile, name='userprofile'),
    path('<pos_id>/comment',views.commentview, name='comment'),
    path('user/follow/<str:username>',views.follow, name='follow'),
    path('search/',Search_User.as_view() , name='search_user'),
    path('about/',views.about_me, name='about'),
    path("<str:username>/edit", EditProfile.as_view(), name="editprofile"),
    
]    

