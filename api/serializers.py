from rest_framework import serializers
from blog.models import Post


# All Post Serializer
class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted', 'username']

    def get_username_from_author(self, posts):
        username = posts.author.username
        return username

    """
        class Meta:
        model = Destination
        fields = '__all__'
    """
