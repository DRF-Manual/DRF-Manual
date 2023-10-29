from django.urls import path
from rest_framework.routers import DefaultRouter
from app.views import ZooViewSet, AnimalViewSet

zoo_list = ZooViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
zoo_detail = ZooViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('zoos/', zoo_list, name='zoo-list'),
    path('zoos/<int:pk>/', zoo_detail, name='zoo-detail'),
]

router = DefaultRouter()
router.register(r'animals', AnimalViewSet, basename='animals')

urlpatterns += router.urls