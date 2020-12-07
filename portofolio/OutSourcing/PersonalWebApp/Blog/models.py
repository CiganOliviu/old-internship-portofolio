from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    introduction = models.TextField(unique=True, default="")

    sub_title_one = models.CharField(max_length=200, unique=True, default="")
    sub_content_one = models.TextField(default="")

    sub_title_two = models.CharField(max_length=200, unique=True, default="")
    sub_content_two = models.TextField(default="")

    sub_title_three = models.CharField(max_length=200, unique=True, default="")
    sub_content_three = models.TextField(default="")

    sub_title_four = models.CharField(max_length=200, unique=True, default="")
    sub_content_four = models.TextField(default="")

    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    update_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    cover_representation = models.ImageField(upload_to='cover_images/', default='default.jpg')
    wallpaper_representation = models.ImageField(upload_to='wallpaper_images/', default='default.jpg')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
