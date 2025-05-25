
from django.urls import path
from my_blogs import views


urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('detail/<int:pk>/', views.blog_detail, name='blog_detail'),
]
