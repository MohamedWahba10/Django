from rest_framework import serializers
from amazon.models import *
class Amazonserlizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=55)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.CharField()
    image=serializers.ImageField()



def create(self,validated_data):
    return Product.objects.create(**validated_data)




def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.price = validated_data.get('price')
        instance.category = validated_data.get('category')
        instance.image = validated_data.get('image')
        instance.save()
        return instance