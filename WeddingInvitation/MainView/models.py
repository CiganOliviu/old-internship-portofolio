from django.db import models
from django.contrib.auth.models import User

class ConfirmAnswer (models.Model):
    answer_sent = models.BooleanField(default = False)
    submitted = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class GuestEnvironmentDetail (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    table_number = models.IntegerField(default = 0)
    table_image = models.ImageField(upload_to = 'guests_tables_images/', blank = True)

    def __str__(self):
        return self.user.first_name
