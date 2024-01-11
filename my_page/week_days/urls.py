from django.urls import path
from . import views

urlpatterns = [
    path('<int:day_number>', views.get_day_number),
    path('<str:day>', views.get_day_name, name='week_day'),
]
