from django.urls import path, re_path
from app.views import zoo_list, ZooDetail, ZooList

urlpatterns = [
    path('zoos/', zoo_list), # 함수형 뷰
    path('zoos/', ZooList.as_view()), # 클래스형 뷰
    re_path(r'^(?P<pk>\d+)/$', ZooDetail.as_view()),
]