from . import jalali
from django.utils import timezone


def jalali_converter(time):
    jmonths = ["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]

    time = timezone.localtime(time)

    get_time = "{},{},{}".format(time.year , time.month , time.day)
    time_to_tuple = jalali.Gregorian(get_time).persian_tuple()
    time_to_list = list(time_to_tuple)
    
    for index , month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    out = "{} {} {},ساعت {}:{}".format(time_to_list[2],time_to_list[1],time_to_list[0],time.hour , time.minute)

    return out