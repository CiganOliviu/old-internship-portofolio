from django.db import models
from django.contrib.auth.models import User


class PlatformPresentationImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return self.name


class ImagesClient(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='specific_user_gallery_images/')
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.name

