from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
# Create your views here.


class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset=Food.objects.all()
    def get_queryset(self):
        """
        This view should return a list of all records
        """
        return Food.objects.all().order_by('name')
    
class FoodImageViewSet(viewsets.ModelViewSet):
    serializer_class = FoodImageSerializer
    queryset = FoodImage.objects.all()
