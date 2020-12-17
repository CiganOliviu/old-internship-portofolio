from django.db import models
from django.contrib.auth.models import User

POSITION = (
    ("Our Guest", "Our Guest"),
    ("Our Bridesmaid", "Our Bridesmaid"),
    ("Our Groomsmen", "Our Groomsmen"),
    ("Our Godparent", "Our Godparent"),
    ("Our Parent", "Our Parent"),
    ("My Husband", "My Husband"),
    ("My Wife", "My Wife"),
)


class ConfirmAnswer (models.Model):
    answer_sent = models.BooleanField(default=False)
    submitted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=25, choices=POSITION, default=0)

    def __str__(self):

        result = str(self.user.first_name) + " " + str(self.user.last_name)

        return result


class GuestEnvironmentDetail (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_number = models.IntegerField(default=0)
    table_image = models.ImageField(upload_to='guests_tables_images/', blank=True)

    def __str__(self):
        
        return self.user.first_name
