from django.urls import path

from . import views

app_name = 'quotes'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create_quote, name='create'),
    path('<int:quote_id>/', views.quote_detail, name='detail'),
    path('<int:quote_id>/delete', views.delete_quote, name='delete'),
    path('<int:quote_id>/requote', views.requote, name='create_requote'),
    path('<int:quote_id>/delete_requote', views.delete_requote, name='delete_requote'),
]