from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:username>/', views.profile, name='profile'),
    path('<slug:username>/followers', views.followers, name='followers'),
    path('<slug:username>/following', views.following, name='followers'),
]