from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import PostSerializer
from blog.models import Post

# Class Base View for all Post GET API
"""
class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
"""


# Function Base View for all post GET API
@api_view(['GET', ])
def api_blog_list(request):
    try:
        queryset = Post.objects.all()
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


# Class Base View for Single  Post GET Update And Delete API
class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):  # Get update and delete
    queryset = Post.objects.all()
    serializer_class = PostSerializer
