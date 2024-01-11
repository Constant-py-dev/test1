from math import pi
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def rectangle(request, width, height):
    response = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {response}')


def square(request, width):
    response = width ** 2
    return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {response}')


def circle(request, radius):
    response = pi * radius ** 2
    return HttpResponse(f'Площадь круга с радиусом {radius} равна {response:.1f}')

def get_rectangle_area(request, width, height):
    reversed_url = reverse('rectangle', args=[width, height])
    return HttpResponseRedirect(reversed_url)


def get_square_area(request, width):
    reversed_url = reverse('square', args=[width])
    return HttpResponseRedirect(reversed_url)

def get_circle_area(request, radius):
    reversed_url = reverse('circle', args=[radius])
    return HttpResponseRedirect(reversed_url)