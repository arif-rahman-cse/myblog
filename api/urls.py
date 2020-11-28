from django.urls import path, include
from .views import ApiBlogPostListView, APIBlogPostCreateView
from .views import api_blog_list
from .views import APIBlogPostDetailView

urlpatterns = [
    # Class Base View Url
    # path('posts/', PostAPIView.as_view(), name='api-blog-posts'),
    path('posts-list/', ApiBlogPostListView.as_view(), name='api-blog-posts'),

    # Url for function base View
    path('posts/', api_blog_list, name='api-blog-posts'),
    path('post/<int:pk>', APIBlogPostDetailView.as_view(), name='api-blog-post-list'),

    path('posts/new', APIBlogPostCreateView.as_view(), name='api-blog-new-post'),
]
