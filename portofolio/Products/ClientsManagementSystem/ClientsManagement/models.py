from django.db import models
from django.contrib.auth.models import User

TYPE_OF_APPS = (
    ("Presentation WebSite", "Presentation WebSite"),
    ("WebApp", "Webapp"),
    ("Mobile App", "Mobile App"),
)

TYPE_OF_CLIENT = (
    ("Small Client", "Small Client"),
    ("Medium Client", "Medium Client"),
    ("Big Client", "Big Client"),
    ("Huge Client", "Huge Client"),
)

PROJECT_STATUS = (
    ("Processing", "Processing"),
    ("Refused", "Refused"),
    ("Accepted", "Accepted"),
)

class ClientInfo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, name = 'user')
    type_of_client = models.CharField(max_length = 100, choices = TYPE_OF_CLIENT, default = "Small Client")
    number_of_finalised_projects = models.IntegerField(default = 0)
    number_of_proposed_projects = models.IntegerField(default = 0)
    number_of_projects_in_progress = models.IntegerField(default = 0)

    def __str__(self):

        return self.user

class FeedBack(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, name = 'user')
    title = models.CharField(max_length = 200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        return self.title

class AskProject(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, name = 'user')
    project_name = models.CharField(max_length = 100)
    project_description = models.TextField()
    list_of_functionalities = models.TextField()
    type = models.CharField(max_length = 100, choices = TYPE_OF_APPS)
    project_status = models.CharField(max_length = 100, choices = PROJECT_STATUS, default = "Processing")
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        return self.project_name

class DirectClientContact(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, name = 'user')
    title = models.CharField(max_length = 100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        return self.title
