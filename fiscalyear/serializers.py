from rest_framework import serializers
from .models import Food, FoodImage



class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImage
        exclude = ['food']

class FoodSerializer(serializers.ModelSerializer):
    food_img = FoodImageSerializer(many =True, required=False)
    class Meta:
        model = Food
        fields = ['name', 'price','food_img']
    
    
    def create(self, validated_data):
        # food_img is not presented in Food Table so it must be poped.
        try: 
            validated_data['food_img']
        except:
            validated_data['food_img'] = []
            
        # Validated data is inserted into Food table after food_img is poped
        food_images = validated_data.pop('food_img')
        food= Food.objects.create(**validated_data)
        
        
    # Now the corresponding value is inserted into FoodImage Table 
        if food_images:
            for image in food_images:
                FoodImage.objects.create(food=food, **image)
        return food
                


