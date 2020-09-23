from django.db import models
from django.contrib.auth.models import User

TYPE_OF_APPS = (
    ("Presentation WebSite", "Presentation WebSite"),
    ("WebApp", "Webapp"),
    ("Mobile App", "Mobile App"),
)

WORKING_STATUS = (
    ("On Queue", "On Queue"),
    ("Current Working at", "Current Working at"),
)

class FinishedProject(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, name = 'user')
    project_name = models.CharField(max_length = 100)
    project_description = models.TextField()
    list_of_functionalities = models.TextField()
    type = models.CharField(max_length = 100, choices = TYPE_OF_APPS)
    date = models.DateTimeField(auto_now_add = True)
    price = models.IntegerField()

    def __str__(self):

        return self.project_name

class ActiveWorkingProject(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, name = 'user')
    project_name = models.CharField(max_length = 100)
    project_description = models.TextField()
    list_of_functionalities = models.TextField()
    type = models.CharField(max_length = 100, choices = TYPE_OF_APPS)
    date = models.DateTimeField(auto_now_add = True)
    price = models.IntegerField()
    ready_for_delivery = models.BooleanField(default = False)

    def __str__(self):

        return self.project_name

class PlannedProject(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, name = 'user')
    project_name = models.CharField(max_length = 100)
    project_description = models.TextField()
    list_of_functionalities = models.TextField()
    type = models.CharField(max_length = 100, choices = TYPE_OF_APPS)
    price = models.IntegerField()
    working_status = models.CharField(max_length = 100, choices = WORKING_STATUS, default = "On Queue")
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        return self.project_name
