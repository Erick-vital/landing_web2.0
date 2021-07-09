from django.shortcuts import redirect, render
from .models import Contacto
from .forms import ContactoForm

# Create your views here.

def index(request):
    form = ContactoForm()

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'demo-freelancer.html')

def about(request):
    return render(request, 'demo-freelancer-about.html')

def form(request):
    form = ContactoForm()

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, 'base.html')
