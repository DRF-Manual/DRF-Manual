from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from app.views import ZooDetail, AnimalDetail, AnimalName

register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('zoo/<int:pk>/', ZooDetail.as_view()),
    path('animal/<str:name>/', AnimalName.as_view()),
    path('animal/<yyyy:birth_year>/', AnimalDetail.as_view()),
]