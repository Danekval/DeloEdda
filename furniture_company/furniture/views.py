from django.shortcuts import render, redirect
from .models import Product, Application
from .forms import ApplicationForm

def index(request):
    return render(request, 'furniture/index.html')

def catalog(request):
    products = Product.objects.all()
    return render(request, 'furniture/catalog.html', {'products': products})

def contacts(request):
    return render(request, 'furniture/contacts.html')

def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ApplicationForm()
    return render(request, 'furniture/application.html', {'form': form})

def success(request):
    return render(request, 'furniture/success.html')