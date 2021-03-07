from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=10, blank=False)
    desired_date = models.DateField()
    sent_moment = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.email
