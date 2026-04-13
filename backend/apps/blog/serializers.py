from rest_framework import serializers
from .models import Post,Category, Heading, PostView


class PostViewSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PostView
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")

class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = [
            "title",
            "slug",
            "level",
            "order"
        ]



class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    headings = HeadingSerializer(many=True)
    views = PostViewSerializer(many=True)
    class Meta: 
        model = Post
        fields = "__all__"



class PostListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    views = PostViewSerializer(many=True)
    class Meta: 
        model = Post
        fields= [
            "id",
            "title",
            "description",
            "thumbnail",
            "slug",
            "category",
            'views'
        ]


