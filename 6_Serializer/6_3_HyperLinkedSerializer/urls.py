from django.urls import path
from .views import AnimalView, ZooView

urlpatterns = [
    path('zoo/<int:pk>/', ZooView.as_view(), name='zoo-detail'),
    path('animal/<int:pk>/', AnimalView.as_view(), name='animal-detail'),

    # How hyperlinked views are determined
    # extra_kwargs
    path('animal/<str:name>/', AnimalView.as_view(), name='animal'),
    path('zoo/<str:zoo_name>/', ZooView.as_view(), name='zoo-detail'),
    # Serializer field
    path('animal/<str:name>/', AnimalView.as_view(), name='animal'),
    path('zoo/<str:zoo_name>/', ZooView.as_view(), name='zoo-name'),
    
    # Changing the URL field name
    path('animal/<str:name>/', AnimalView.as_view(), name='animal'),
    path('zoo/<str:zoo_name>/', ZooView.as_view(), name='zoo-detail'),
]