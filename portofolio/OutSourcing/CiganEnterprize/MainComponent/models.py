from django.db import models

COUNTRY = (
    ("Romania", "Romania"),
)


class Studio(models.Model):

    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=200, unique=True, default="")
    address = models.CharField(max_length=200, unique=True, default="")
    country = models.CharField(max_length=100, choices=COUNTRY, default="Romania")
    description = models.TextField(default="")

    studio_image = models.ImageField(upload_to='studio_image/', default='default.jpg')
    manager_name = models.CharField(max_length=200, default="")
    manager_image = models.ImageField(upload_to='managers_image/', default='default.jpg')
    manager_words = models.TextField(default="")

    gallery_image_one = models.ImageField(upload_to='studios_gallery_images/', default='default.jpg')
    gallery_image_two = models.ImageField(upload_to='studios_gallery_images/', default='default.jpg')
    gallery_image_three = models.ImageField(upload_to='studios_gallery_images/', default='default.jpg')
    gallery_image_four = models.ImageField(upload_to='studios_gallery_images/', default='default.jpg')
    gallery_image_five = models.ImageField(upload_to='studios_gallery_images/', default='default.jpg')

    studio_slug = models.SlugField(max_length=200, unique=True, default="")
    moment = models.DateTimeField()

    def __str__(self):

        return self.city
