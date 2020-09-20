from django.urls import path

from . import views

app_name = 'quotes'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='create'),
    path('<int:quote_id>/', views.detail, name='detail'),
    path('<int:quote_id>/delete', views.delete, name='delete'),
]