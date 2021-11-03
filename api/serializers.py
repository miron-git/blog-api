from rest_framework import serializers

from .models import Post, Comment, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    #author = serializers.SlugRelatedField(slug_field='id', read_only = True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.SlugRelatedField(slug_field='id', read_only = True)
    
    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'slug')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only = True)
    

    class Meta:
        fields = ('user', 'author')
        model = Follow