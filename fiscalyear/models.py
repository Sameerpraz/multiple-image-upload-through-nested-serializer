from django.db import models
import datetime
# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
class FoodImage(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE,related_name='food_img')
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return f'{self.id}'