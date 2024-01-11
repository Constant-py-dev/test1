from django.urls import path, register_converter
from . import views, converters

register_converter(converters.DateConverter, 'date')

urlpatterns = [
    path('', views.index),
    path('<date:date>', views.get_date),
    path('elements', views.get_elements),
    path('elements/<element>', views.get_element, name='element'),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('<int:num>', views.get_znak_zodiac_from_num),
    path('<znak_zodiac>', views.get_znak_zodiac, name='horoscope-name'),
]
