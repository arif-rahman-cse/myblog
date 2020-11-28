from rest_framework import serializers
from blog.models import Post, TestPost


# All Post Serializer
class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = Post
        fields = ['id', 'referral_code', 'title', 'content', 'date_posted', 'username']

    def get_username_from_author(self, posts):
        username = posts.author.username
        return username

    """
        class Meta:
        model = Destination
        fields = '__all__'
    """


class TestPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPost

        fields = ['title', 'author', ]
        read_only_fields = ['invoice_no', ]
