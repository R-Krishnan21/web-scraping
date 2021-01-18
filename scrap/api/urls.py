from django.urls import path, include
from .views import index, Question, latest
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('question', Question, basename='q')

urlpatterns = [
    path('', index),
    path('latest/', latest),
    path('', include(router.urls))
]