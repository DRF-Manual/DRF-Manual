from django.urls import path
from app.views import AnimalList, AnimalDetail, AnimalName

app_name = 'animal'  # 애플리케이션 네임스페이스 지정

urlpatterns = [
    path('animals/', AnimalList.as_view(), name='list'),
    path('animals/birth_year/<int:birth_year>/', AnimalDetail.as_view(), name='by_birth_year'),
    path('animals/name/<str:name>/', AnimalName.as_view(), name='by_name'),
]