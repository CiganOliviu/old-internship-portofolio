from django.db import models
from ProjectsManagement.models import TYPE_OF_APPS

COUNTRY = (
    ("Romania", "Romania"),
)

CAREER = (
    ("Marketing Specialist", "Marketing Specialist"),
    ("Web QA", "Web QA"),
    ("Mobile QA", "Mobile QA"),
    ("Software Developer", "Software Developer"),
    ("Web Developer", "Web Developer"),
    ("Web Designer", "Web Designer"),
    ("Mobile Developer", "Mobile Developer"),
    ("Founder", "Founder"),
    ("CoFounder", "CoFounder"),
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


class Employer(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    post = models.CharField(max_length=150, choices=CAREER)
    experience = models.IntegerField()

    profile_image = models.ImageField(upload_to='employers_images/')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Project(models.Model):

    id = models.AutoField(primary_key=True)
    name_of_project = models.CharField(max_length=150)
    project_image = models.ImageField(upload_to='projects_images/')
    field = models.CharField(max_length=150, choices=TYPE_OF_APPS)

    def __str__(self):
        return self.name_of_project
