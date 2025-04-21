from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FurnitureViewSet, HomePageView, CatalogView, ContactsView, ApplicationView, SuccessView

router = DefaultRouter()
router.register(prefix='furniture', viewset=FurnitureViewSet)  # Исправлено: добавлены именованные аргументы

urlpatterns = [
    path('api/', include(router.urls)),  # Добавлен префикс 'api/' для API
    path('', HomePageView.as_view(), name='index'),  # Корневой URL приложения
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('application/', ApplicationView.as_view(), name='application'),
    path('application/success/', SuccessView.as_view(), name='application_success'),
]