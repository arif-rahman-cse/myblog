from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers import PostSerializer, TestPostSerializer
from blog.models import Post, TestPost

# Class Base View for all Post GET API
"""
class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
"""


# Function Base View for all blog post GET API
@api_view(['GET', ])
def api_blog_list(request):
    try:
        queryset = Post.objects.all()
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


# Class Base View for Single  Blog Post GET Update And Delete API
class APIBlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):  # Get update and delete
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Post ListView Pagination
class ApiBlogPostListView(ListAPIView, ):
    permission_classes = (IsAuthenticated,)  # Restrict  Post List API
    queryset = Post.objects.all()  # It will get all the posts and pass through context through template
    serializer_class = PostSerializer  # Set Serializer Class
    pagination_class = PageNumberPagination  # Pagination Class


class APIBlogPostCreateView(generics.CreateAPIView):
    queryset = TestPost.objects.all()
    serializer_class = TestPostSerializer
