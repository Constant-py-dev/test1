from django.shortcuts import render
from datetime import date
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

elements = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

dates = {
    (1, 32): 'aries',
    (32, 63): 'taurus',
    (63, 94): 'gemini',
    (94, 125): 'cancer',
    (125, 155): 'leo',
    (155, 188): 'virgo',
    (188, 218): 'libra',
    (218, 248): 'scorpio',
    (248, 278): 'sagittarius',
    (278, 307): 'capricorn',
    (307, 337): 'aquarius',
    (337, 366): 'pisces'
}

def get_list(request, lst):
    return HttpResponse(f'list ---> {lst}')

def get_date(request, date):
    return HttpResponse(f'Дата ---> {date}')


def menu_handler(lst, viewname):
    list_items = ''
    for item in lst:
        url = reverse(viewname, args=[item])
        list_items += f'<li><a href={url}>{item.title()}</a></li>'
    response = f"""
        <ul>
            {list_items}
        <ul>
        """
    return response


def index(request):
    lst_zodiac = list(zodiac_dict)
    response = menu_handler(lst_zodiac, 'horoscope-name')
    return HttpResponse(response)


def get_elements(request):
    element_list = list(elements)
    response = menu_handler(element_list, 'element')
    return HttpResponse(response)


def get_element(request, element):
    element_list = elements.get(element, None)
    response = menu_handler(element_list, 'horoscope-name')
    return HttpResponse(response)


def get_info_by_date(request, month, day):
    try:
        input_date = date(1, month, day)
    except ValueError:
        return HttpResponseNotFound('Неверное значение даты!')
    day_number = int(input_date.strftime('%j')) - 79
    if day_number <= 0:
        day_number += 365
    for k, v in dates.items():
        if day_number in range(*k):
            url = reverse('horoscope-name', args=[v])
            return HttpResponseRedirect(url)


def get_znak_zodiac(request, znak_zodiac):
    response = zodiac_dict.get(znak_zodiac, None)
    if response:
        return HttpResponse(f'<h2>{response}</h2>')
    else:
        return HttpResponseNotFound(f'Неизвестный знак зодиака - {znak_zodiac}')


def get_znak_zodiac_from_num(request, num):
    lst_zodiac = list(zodiac_dict)
    if num > len(lst_zodiac):
        return HttpResponseNotFound(f'Неизвестный номер зодиака - {num}')
    zodiac_name = lst_zodiac[num - 1]
    reverse_url = reverse('horoscope-name', args=[zodiac_name])
    return HttpResponseRedirect(reverse_url)
