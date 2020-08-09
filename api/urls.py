from django.urls import path
# from .views import PostAPIView
from .views import api_blog_list
from .views import PostAPIDetailView

urlpatterns = [
    # Class Base View Url
    # path('posts/', PostAPIView.as_view(), name='api-blog-posts'),

    # Url for function base View
    path('posts/', api_blog_list, name='api-blog-posts'),
    path('posts/<int:pk>', PostAPIDetailView.as_view(), name='api-single-blog-post'),
]
