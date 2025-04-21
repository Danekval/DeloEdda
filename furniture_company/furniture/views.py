from django.http import HttpResponseRedirect
from rest_framework import viewsets
from django.urls import reverse_lazy
from .models import Furniture
from .serializers import FurnitureSerializer
from django.views.generic import TemplateView, CreateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ApplicationForm
from .models import Application
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# furniture/views.py
class HomePageView(TemplateView):
    template_name = 'furniture/index.html'  # Путь внутри папки templates

class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

class CatalogView(TemplateView):
    template_name = 'furniture/catalog.html'  # Путь к шаблону

class ContactsView(TemplateView):
    template_name = 'furniture/contacts.html'


class ApplicationView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'furniture/application.html'
    success_url = reverse_lazy('application_success')  # Используем прямое имя URL

    def form_valid(self, form):
        # Сохраняем форму, но не вызываем super()
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

class SuccessView(TemplateView):
    template_name = 'furniture/application_success.html'
class ApplicationAPIView(APIView):
    def post(self, request):
        # Обработка данных
        return Response({"success": True}, status=200)