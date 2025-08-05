from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_comment, name='create_comment'),
    path('<int:comment_id>/update/', views.update_comment, name='update_comment'),
    path('<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:comment_id>/replies/', views.comment_replies, name='comment_replies'),
]