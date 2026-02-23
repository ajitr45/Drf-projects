from rest_framework import serializers
from .models import Blog, Comment



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many= True, read_only = True)  # using nested serializiers to fetch the comments in Blogs
    class Meta:
        model = Blog
        fields = '__all__'