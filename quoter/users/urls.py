from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('edit/', views.edit_profile, name='edit'),
    path('<slug:username>/', views.profile, name='profile'),
    path('<slug:username>/follow', views.follow_user, name='follow'),
    path('<slug:username>/unfollow', views.unfollow_user, name='unfollow'),
    path('<slug:username>/followers', views.followers, name='followers'),
    path('<slug:username>/following', views.following, name='following'),
]
