from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('contacts/', views.contacts, name='contacts'),
    path('application/', views.application, name='application'),
    path('success/', views.success, name='success'),
]