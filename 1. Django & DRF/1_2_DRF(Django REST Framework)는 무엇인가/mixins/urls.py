urlpatterns = [
    path('mixin/models/', ModelsAPIMixins.as_view()),
    path('mixin/model/<int:pk>/', ModelAPIMixins.as_view()),
]