from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=10, blank=False)
    desired_date = models.DateField()
    sent_moment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class AdminResponse(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.DateField()
    location = models.CharField(max_length=100, blank=False)
    response_moment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client

