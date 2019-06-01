from django.shortcuts import render

# Create your views here.
from .models import Car

"""
Функция отображения для домашней страницы сайта.
"""
def index(request): 
    # Генерация "количеств" некоторых главных объектов
    num_cars = Car.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={
            'num_cars':num_cars,
        },
    )

from django.views import generic

class CarListView(generic.ListView):
    model = Car

class CarDetailView(generic.DetailView):
    model = Car
