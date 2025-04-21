from rest_framework import serializers
from furniture.models import Furniture  # Импорт модели из приложения furniture

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'  # Все поля модели