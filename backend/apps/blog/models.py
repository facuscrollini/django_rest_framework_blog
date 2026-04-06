from django.db import models
from django.utils import timezone

# Create your models here.

def blog_thumbnail_directory(instance, filename):
    return "blog/{0}/{1}".format(instance.title, filename)

class Post(models.Model):


    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    status_options = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    title = models.CharField()
    description = models.CharField(max_length=128)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to=blog_thumbnail_directory)

    keywords = models.CharField(max_length=200)
    slug = models.CharField(max_length=128)


    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=status_options, default="draft")
    category = models.CharField()
    autor = models.CharField()