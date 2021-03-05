from django.db import models
from django.contrib.auth.models import User

COLUMN_NUMBER = (
    ("First Column", "First Column"),
    ("Second Column", "Second Column"),
    ("Third Column", "Third Column"),
    ("Fourth Column", "Fourth Column"),
)


PART_OF_CATALOGUE = (
    ("Cover Image", "Cover Image"),
    ("Content Image", "Content Image"),
    ("Back Image", "Back Image"),
    ("None of it", "None of it"),
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
    column = models.CharField(max_length=255, choices=COLUMN_NUMBER, default="First Column")
    image_slug = models.SlugField(max_length=200, default="")

    def __str__(self):
        return self.name


class ClientCatalogue(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='clients_catalogue/')
    image_positioning = models.CharField(max_length=255, choices=PART_OF_CATALOGUE, default="None of it")

    def __str__(self):
        return str(self.client)