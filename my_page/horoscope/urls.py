from django.urls import path, register_converter, converters
from . import views, converters

register_converter(converters.DateConverter, 'date')
register_converter(converters.SplitConverter, "split-list")
register_converter(converters.UpperConvertor, 'upper')

urlpatterns = [
    path('', views.index),
    path('elements', views.get_elements),
    path('elements/<element>', views.get_element, name='element'),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('<int:num>', views.get_znak_zodiac_from_num, name='horoscope-number'),
    path('<znak_zodiac>', views.get_znak_zodiac, name='horoscope-name'),
]
