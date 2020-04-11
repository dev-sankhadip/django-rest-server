from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AppViewSet

router=DefaultRouter();
router.register(r'app',AppViewSet, basename='app')

urlpatterns=router.urls