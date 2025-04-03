from django.contrib import admin
from .models import Product, Application
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')  # Какие поля показывать в списке
    search_fields = ('name', 'description')  # По каким полям можно искать
    list_filter = ('created_at',)  # Фильтры справа

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    search_fields = ('name', 'phone', 'email')
# Register your models here.
