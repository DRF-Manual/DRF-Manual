from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter # pip install drf-nested-routers 필요
from app.views import ZooViewSet, AnimalViewSet

router = DefaultRouter()
router.register(r'zoos', ZooViewSet, basename='zoos')

simple_router = SimpleRouter()
simple_router.register(r'zoos_simple', ZooViewSet, basename='zoos_simple')

nested_router = NestedSimpleRouter(router, r'zoos', lookup='zoos')
nested_router.register(r'animals', AnimalViewSet, basename='animals')

urlpatterns = router.urls + simple_router.urls + nested_router.urls