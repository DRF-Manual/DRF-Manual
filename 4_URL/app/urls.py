from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AnimalViewSet

router = DefaultRouter()
router.register(r'animals', AnimalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('4_2/', include('4_2_URL패턴_정의.urls')),
    path('4_3/', include('4_3_경로_변환자.urls')),
    # 인스턴스 네임스페이스 지정
    path('4_4/a/', include('4_4_네임스페이싱.urls', namespace='admin')),
    path('4_4/b/', include(router.urls, namespace='user')), # router에 네임스페이스 지정
    path('4_6/', include('4_6_충돌하는_URL패턴.urls')),
    path('4_7/', include('4_7_DRF의_URL_처리.urls')),
    path('4_8/', include('4_8_라우터.urls')),
]
