from django.db import models


class NewsLetter(models.Model):

    email = models.EmailField(max_length=248)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.email


class Contact(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):

        return self.title
