from django.urls import path
from .views import post_list, post_by_category, post_detail, add_comment_to_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post_by_category/<str:category>/', post_by_category, name='post_by_category'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('add_comment/<int:post_id>/', add_comment_to_post, name='add_comment_to_post'),
]