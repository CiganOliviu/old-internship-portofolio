from datetime import datetime

from .models import Studio


def update_date_in_studios():

    studios_objects = Studio.objects.all()

    for studio_object in studios_objects:

        studio_object.moment = datetime.now()
        studio_object.save()
