from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
week_days_dict = {'monday': 'понедельник',
                  'tuesday': 'вторник',
                  'wednesday': 'среда',
                  'thursday': 'четверг',
                  'friday': 'пятница',
                  'saturday': 'суббота',
                  'sunday': 'воскресенье'
                  }


def get_day_name(request, day):
    day_name = week_days_dict.get(day, None)
    if not day_name:
        return HttpResponseNotFound(f'Неизвестный  день недели - {day}')
    return HttpResponse(f'Сегодня  день недели {day_name}')

def get_day_number(request, day_number):
    day_list = list(week_days_dict)
    if day_number > len(day_list):
        return HttpResponseNotFound(f'Неизвестный  день недели - {day_number}')
    day = day_list[day_number-1]
    reverse_url = reverse('week_day', args = [day])
    return HttpResponseRedirect(reverse_url)