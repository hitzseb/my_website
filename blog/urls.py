from django.urls import path
from .views import *

urlpatterns = [
    # user
    path('', blog, name='blog'),
    path('post_by_category/<str:category>/', post_by_category, name='post_by_category'),
    path('post/<int:pk>/', post, name='post'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
    # admin
    path('admin/', admin, name='admin'),
    path('post/create/', post_form, name='post_create'),
    path('post/edit/<int:pk>/', post_form, name='post_edit'),
    path('post/delete/<int:pk>/', post_delete, name='post_delete'),
    path('category/create/', category_form, name='category_create'),
    path('category/edit/<int:pk>/', category_form, name='category_edit'),
    path('category/delete/<int:pk>/', category_delete, name='category_delete'),
    path('add_response/<int:comment_id>/', add_response, name='add_response'),
]