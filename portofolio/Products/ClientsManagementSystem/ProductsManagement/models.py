from django.db import models

TYPE_OF_APPS = (
    ("Presentation WebSite", "Presentation WebSite"),
    ("WebApp", "Webapp"),
    ("Mobile App", "Mobile App"),
)

WORKING_STATUS = (
    ("On Queue", "On Queue"),
    ("Current Working at", "Current Working at"),
)

class FinishedProduct(models.Model):
    id = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length = 100)
    product_description = models.TextField()
    list_of_functionalities = models.TextField()
    type = models.CharField(max_length = 100, choices = TYPE_OF_APPS)
    date = models.DateTimeField(auto_now_add = True)
    price = models.IntegerField()

class ActiveWorkingProduct(models.Model):
    id = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length = 100)
    product_description = models.TextField()
    list_of_functionalities = models.TextField()
    type = models.CharField(max_length = 100, choices = TYPE_OF_APPS)
    price = models.IntegerField()
    ready_for_delivery = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add = True)

class PlannedProduct(models.Model):
    id = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length = 100)
    product_description = models.TextField()
    list_of_functionalities = models.TextField()
    type = models.CharField(max_length = 100, choices = TYPE_OF_APPS)
    price = models.IntegerField()
    working_status = models.CharField(max_length = 100, choices = WORKING_STATUS, default = "On Queue")
    date = models.DateTimeField(auto_now_add = True)
