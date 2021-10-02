from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/images/', views.image_list, name='image_list'),
    path('api/images/<int:pk>/', views.image_detail, name='image_detail'),
    path('api/images/<int:pk>/resize/', views.resize_picture, name='resize_picture'),
    path('api/images/<int:pk>/rotate/', views.rotate_picture, name='rotate_picture'),
]