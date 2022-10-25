from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('home',views.home, name='home'),
    path('setting',views.setting, name='setting'),
    path('like_post',views.like_post, name='like_post'),
    path('edit_post',views.edit_post, name='edit_post'),
    path('delete_post',views.delete_post, name='delete_post'),
    path('profile/<str:pk>',views.profile, name='profile'),
    path('search',views.search, name='search'),
    path('follow',views.follow, name='folow'),
    path('upload',views.upload, name='upload'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('logout',views.logout, name='logout'),
]
