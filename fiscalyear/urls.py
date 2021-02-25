from django.urls import path
from .views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('food', FoodViewSet)
router.register('foodimage', FoodImageViewSet)
urlpatterns = [
]+router.urls
