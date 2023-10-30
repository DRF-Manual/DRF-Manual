from django.urls import path, register_converter
from app.views import new_animal, AnimalName, AnimalDetail
from .converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('animals/new/', new_animal),
    path('animals/<yyyy:birth_year>/', AnimalDetail.as_view()),
    path('animals/<str:name>/', AnimalName.as_view()),
]