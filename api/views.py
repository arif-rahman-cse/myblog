from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import PostSerializer
from blog.models import Post


# Class Base View
"""
class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
"""


# Function Base View
@api_view(['GET', ])
def api_blog_list(request):
    try:
        queryset = Post.objects.all()
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
