from django.contrib import admin
# Если у вас есть другие модели, импортируйте их здесь
from .models import Furniture
from .models import Application # Пример для модели Furniture

# Зарегистрируйте ваши модели

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')