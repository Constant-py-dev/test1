from django.urls import path, include
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.rectangle, name='rectangle'),
    path('square/<int:width>', views.square, name='square'),
    path('circle/<int:radius>', views.circle, name='circle'),
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area),
    path('get_square_area/<int:width>', views.get_square_area),
    path('get_circle_area/<int:radius>', views.get_circle_area),
]
