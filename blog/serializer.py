from rest_framework import serializers
from .models import Post
from .models import Post, Category,Comment
from account.serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=250)
    slug = serializers.SlugField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    publish_time = serializers.DateTimeField()
    draft = serializers.BooleanField()
    image = serializers.ImageField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)


    def validate_slug(self, slug):
        try:
            q = Post.objects.get(slug=slug)
            raise serializers.ValidationError("slug must be unique")
        except Post.DoesNotExist:
            return slug



    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.content = validated_data.get('content', instance.content)
        instance.publish_time = validated_data.get('publish_time', instance.publish_time)
        instance.draft = validated_data.get('draft', instance.draft)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    is_confirmed = serializers.BooleanField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.content = validated_data.get('content', instance.content)
        instance.create_at = validated_data.get('create_at', instance.create_at)
        instance.update_at = validated_data.get('update_at', instance.update_at)
        instance.save()
        return instance


    # author_detail = UserSerializer(source='author', read_only=True)
    # class Meta:
    #     model = Comment
    #     fields = "__all__"