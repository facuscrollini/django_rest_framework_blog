from django.urls import path,include

from .views import PostListView, PostDetailView, PostHeadingsView



urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('posts/<str:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<str:slug>/headings', PostHeadingsView.as_view(), name="post-headings")
]