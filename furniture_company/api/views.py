from rest_framework import viewsets
from furniture.models import Furniture  # Импорт модели
from .serializers import FurnitureSerializer  # Импорт сериализатора

class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer