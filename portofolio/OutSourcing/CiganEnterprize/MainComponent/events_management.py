from datetime import date

from Events.models import PastEvent, SponsorEvent, HostEvent

def get_current_time():

    result = date.today()

    return result

def check_event_day_availability(event_day):

    current_day = get_current_time().day

    if current_day > event_day:
        return False

    return True

def check_event_month_availability(event_month):

    current_month = get_current_time().month

    if current_month > event_month:
        return False

    return True

def check_event_year_availability(event_year):

    current_year = get_current_time().year

    if current_year > event_year:
        return False

    return True

def check_if_event_happens_today(event_database_object):

    current_day = get_current_time().day
    current_month = get_current_time().month
    current_year = get_current_time().year

    if event_database_object.date.year == current_year:
        if event_database_object.date.month == current_month:
            if event_database_object.date.day == current_day:
                return True

    return False

def check_current_host_event_availability(event):

    if check_event_day_availability(event.date.day):
        if check_event_month_availability(event.date.month):
            if check_event_year_availability(event.date.year):
                return True

    return False

def add_event_to_past_events(event):

    if not PastEvent.objects.filter(event_name = event.event_name, location = event.location, space = event.space, part_of_event = event.part_of_event, introduction = event.introduction, about_event = event.about_event, get_tickets = event.get_tickets, location_image = event.location_image, date = event.date, past_event_slug = event.event_slug).exists():
        save_to_database = PastEvent(event_name = event.event_name, location = event.location, space = event.space, part_of_event = event.part_of_event, introduction = event.introduction, about_event = event.about_event, get_tickets = event.get_tickets, location_image = event.location_image, date = event.date, past_event_slug = event.event_slug)
        save_to_database.save()

def delete_event_from_current_database_events(database, event):

    database.objects.filter(event_name = event.event_name, location = event.location).delete()

def fetch_host_event_database():

    current_host_events = HostEvent.objects.all()

    for event in current_host_events:

        if not check_current_host_event_availability(event):
            add_event_to_past_events(event)
            delete_event_from_current_database_events(HostEvent, event)

def fetch_sponsor_event_database():

    current_sponsor_events = SponsorEvent.objects.all()

    for event in current_sponsor_events:

        if not check_current_host_event_availability(event):
            add_event_to_past_events(event)
            delete_event_from_current_database_events(SponsorEvent, event)
