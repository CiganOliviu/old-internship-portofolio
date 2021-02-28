from django.db import models
from MainComponent.models import Studio

JOB_TYPE = (
    ("Remote", "Remote"),
    ("OnSite", "OnSite"),
)


class AvailableJob(models.Model):

    id = models.AutoField(primary_key=True)
    post = models.CharField(max_length=150, unique=False, default="")
    location = models.ForeignKey(Studio, on_delete=models.CASCADE, default=1)
    description = models.TextField(default="")
    requirements = models.TextField(default="")
    one_day = models.TextField(default="")
    job_type = models.CharField(max_length=100, choices=JOB_TYPE, default="OnSite")
    perks = models.CharField(max_length=200, default="")
    released_day = models.DateTimeField(auto_now_add=True)
    job_slug = models.SlugField(max_length=200, unique=True, default="")

    representation_image = models.ImageField(upload_to='jobs_representation_images/', default="default.jpg")

    def __str__(self):

        return str(self.post) + " | " + str(self.location) + " | " + str(self.job_type)


class AvailableInternship(models.Model):

    id = models.AutoField(primary_key=True)
    post = models.CharField(max_length=150, unique=False, default="")
    location = models.ForeignKey(Studio, on_delete=models.CASCADE, default=1)
    description = models.TextField(default="")
    requirements = models.TextField(default="")
    one_day = models.TextField(default="")
    job_type = models.CharField(max_length=100, choices=JOB_TYPE, default="OnSite")
    perks = models.CharField(max_length=200, default="")
    released_day = models.DateTimeField(auto_now_add=True)
    internship_slug = models.SlugField(max_length=200, unique=True, default="")

    representation_image = models.ImageField(upload_to='internship_representation_images/', default="default.jpg")

    def __str__(self):

        return str(self.post) + " " + str(self.location)


class JobsAppliance(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    years_of_experience = models.PositiveIntegerField(default=0)
    curriculum_vitae = models.FileField("upload_tcurriculum_vitae/", default='default.pdf')
    description_of_skills = models.TextField(default="")
    career = models.ForeignKey(AvailableJob, on_delete=models.CASCADE, default=1)
    accepted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.first_name) + " " + str(self.last_name)


class InternshipsAppliance(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    curriculum_vitae = models.FileField(upload_to="internships_curriculum_vitae/", default='default.pdf')
    description_of_skills = models.TextField(default="")
    career = models.ForeignKey(AvailableInternship, on_delete=models.CASCADE, default=1)
    accepted = models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.first_name) + " " + str(self.last_name)
