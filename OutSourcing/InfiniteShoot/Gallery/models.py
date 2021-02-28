from django.db import models
from django.contrib.auth.models import User

COLUMN_NUMBER = (
    ("First Column", "First Column"),
    ("Second Column", "Second Column"),
    ("Third Column", "Third Column"),
    ("Fourth Column", "Fourth Column"),
)


BOOLEAN_ANSWER = (
    ("YES", "YES"),
    ("NO", "NO"),
)


class PlatformPresentationImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')
    column = models.CharField(max_length=255, choices=COLUMN_NUMBER, default="First Column")

    def __str__(self):
        return self.name


class ImagesClient(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='specific_user_gallery_images/')
    our_thoughts = models.TextField(blank=False, default="")

    pick_cover_image = models.CharField(max_length=5, choices=BOOLEAN_ANSWER, default="NO")
    pick_content_image_one = models.CharField(max_length=5, choices=BOOLEAN_ANSWER, default="NO")
    pick_content_image_two = models.CharField(max_length=5, choices=BOOLEAN_ANSWER, default="NO")
    pick_content_image_three = models.CharField(max_length=5, choices=BOOLEAN_ANSWER, default="NO")
    pick_content_image_four = models.CharField(max_length=5, choices=BOOLEAN_ANSWER, default="NO")
    pick_back_image = models.CharField(max_length=5, choices=BOOLEAN_ANSWER, default="NO")

    column = models.CharField(max_length=255, choices=COLUMN_NUMBER, default="First Column")
    image_slug = models.SlugField(max_length=200, default="")

    def __str__(self):
        return self.name
