from django.urls import path

from . import views

app_name = 'quotes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:quote_id>/', views.detail, name='detail'),
]