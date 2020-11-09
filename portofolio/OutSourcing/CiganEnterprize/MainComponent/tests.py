from datetime import date


def get_current_time():

    result = date.today()

    return result


def is_event_out_of_day(event_day):

    current_day = get_current_time().day

    if current_day > event_day:
        return True

    return False


def is_the_day_match(event_day):

    current_day = get_current_time().day

    if current_day == event_day:
        return True

    return False


def is_event_out_of_month(event_month):

    current_month = get_current_time().month

    if current_month > event_month:
        return True

    return False


def is_the_month_match(event_month):

    current_month = get_current_time().month

    if current_month == event_month:
        return True

    return False


def is_event_out_of_year(event_year):

    current_year = get_current_time().year

    if current_year > event_year:
        return True

    return False


def is_the_year_match(event_year):

    current_year = get_current_time().year

    if current_year == event_year:
        return True

    return False


def check_current_event_availability(event):

    if is_event_out_of_year(event.year):
        return True

    if is_the_year_match(event.year):
        if is_event_out_of_month(event.month):
            return True

    if is_the_month_match(event.month):
        if is_event_out_of_day(event.day):
            return True

    return False


def test_is_event_out_of_day():

    is_event_out_of_day(25)

    assert is_event_out_of_day(25) == False
    assert is_event_out_of_day(22) == False
    assert is_event_out_of_day(13 == True)


def test_is_the_day_match():

    assert is_the_day_match(22) == True
    assert is_the_day_match(23) == False
    assert is_the_day_match(30) == False


def test_is_event_out_of_month():

    assert is_event_out_of_month(10) == False
    assert is_event_out_of_month(12) == False
    assert is_event_out_of_month(7) == True


def test_is_the_month_match():

    assert is_the_month_match(10) == True
    assert is_the_month_match(12) == False
    assert is_the_month_match(5) == False


def test_is_event_out_of_year():

    assert is_event_out_of_year(2020) == False
    assert is_event_out_of_year(2019) == True
    assert is_event_out_of_year(2032) == False


def test_is_the_year_match():

    assert is_the_year_match(2020) == True
    assert is_the_year_match(2012) == False
    assert is_the_year_match(2082) == False


def test_check_event_availability():

    event_one = date(day=12, month=10, year=2020)
    event_two = date(day=22, month=10, year=2021)
    event_three = date(day=22, month=7, year=2013)
    event_four = date(day=22, month=10, year=2020)

    assert check_current_event_availability(event_one) == True
    assert check_current_event_availability(event_two) == False
    assert check_current_event_availability(event_three) == True
    assert check_current_event_availability(event_four) == False


test_is_event_out_of_day()
test_is_the_day_match()
test_is_event_out_of_month()
test_is_the_month_match()
test_is_event_out_of_year()
test_is_the_year_match()
test_check_event_availability()