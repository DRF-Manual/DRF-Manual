from rest_framework import routers
from .views import ModelViewSet

router = routers.SimpleRouter()
router.register('models', ModelViewSet)

urlpatterns = router.urls
