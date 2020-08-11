from rest_framework import serializers
from blog.models import Post


# All Post Serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted']

    """
        class Meta:
        model = Destination
        fields = '__all__'
    """
