from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('edit/', views.edit_profile, name='edit'),
    path('<slug:username>/', views.profile, name='profile'),
]
