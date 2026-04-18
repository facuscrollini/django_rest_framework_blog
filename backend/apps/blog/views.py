from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post, Heading, PostView, PostAnalytics
from .serializers import PostListSerializer, PostSerializer, HeadingSerializer, PostViewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import get_client_ip

class PostListView(APIView):
    def get(self, request, *args, **kwargs):
        posts  = Post.postobjects.all()
        serialized_posts = PostListSerializer(posts, many=True).data
        return Response(serialized_posts)
    


class PostDetailView(APIView):
    def get(self, request, slug):
        post = Post.postobjects.get(slug=slug)
        serialized_post = PostSerializer(post).data

        #Increment post view count
        post_analytics = PostAnalytics.objects.get(post=post)
        post_analytics.increment_view(request)

        return Response(serialized_post)





class PostHeadingsView(ListAPIView):
   
    serializer_class = HeadingSerializer

    def get_queryset(self):
        post_slug = self.kwargs.get("slug")
        return Heading.objects.filter(post__slug = post_slug)
