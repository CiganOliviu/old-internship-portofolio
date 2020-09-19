from django.db import models

class PastEvent(models.Model):

    event_name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    space = models.CharField(max_length = 200)
    part_of_event = models.CharField(max_length = 200, blank = True)
    introduction = models.CharField(max_length = 300, default = "")
    about_event = models.TextField(default = "")
    get_tickets = models.URLField(max_length = 200)

    location_image = models.ImageField(upload_to='events/locations/', default='default.jpg')
    date = models.DateTimeField()

    past_event_slug = models.SlugField(max_length = 200, unique = True, default = "")

    def __str__(self):

        return self.event_name

class SponsorEvent(models.Model):

    event_name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    space = models.CharField(max_length = 200)
    part_of_event = models.CharField(max_length = 200, blank = True)
    introduction = models.CharField(max_length = 300, default = "")
    about_event = models.TextField(default = "")
    get_tickets = models.URLField(max_length = 200)

    location_image = models.ImageField(upload_to='events/locations/', default='default.jpg')
    date = models.DateTimeField()

    event_slug = models.SlugField(max_length = 200, unique = True, default = "")

    def __str__(self):

        return self.event_name

class HostEvent(models.Model):

    event_name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    space = models.CharField(max_length = 200)
    part_of_event = models.CharField(max_length = 200, blank = True)
    introduction = models.CharField(max_length = 300, default = "")
    about_event = models.TextField(default = "")
    get_tickets = models.URLField(max_length = 200)

    location_image = models.ImageField(upload_to='events/locations/', default='default.jpg')
    date = models.DateTimeField()

    event_slug = models.SlugField(max_length = 200, unique = True, default = "")

    def __str__(self):

        return self.event_name
