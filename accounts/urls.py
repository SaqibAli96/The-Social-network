
from django.contrib import admin
from django.urls import path
from accounts import views 

urlpatterns = [
    
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('user_login2', views.user_login2, name='user_login2'),
    path('change_password', views.Change_Password.as_view(), name='change_password'),
]
