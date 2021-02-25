from django.contrib import admin
from .models import *

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name','price']

class FoodImageAdmin(admin.ModelAdmin):
    list_display = ['food','image']

admin.site.register(Food, FoodAdmin)
admin.site.register(FoodImage,FoodImageAdmin)




