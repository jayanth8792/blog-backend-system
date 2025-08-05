from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('my-blogs/', views.my_blogs, name='my_blogs'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:blog_id>/comments/', views.blog_comments, name='blog_comments'),
]