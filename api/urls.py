from django.urls import path
# from .views import PostAPIView
from .views import api_blog_list

urlpatterns = [
    # Class Base View Url
    # path('posts/', PostAPIView.as_view(), name='api-blog-posts'),

    # Url for function base View
    path('posts/', api_blog_list, name='api-blog-posts'),
]
