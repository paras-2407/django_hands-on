from django.shortcuts import render
from .models import Student
# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'first_app/index.html')

def home(request):
    return render(request, 'first_app/home.html')
    
def about(request):
    return render(request, 'first_app/about.html')

def contact(request):
    return render(request, 'first_app/contact.html')

def login(request):
    return render(request, 'first_app/login.html')

def services(request):
    return render(request, 'first_app/services.html')



def new_index(request):
    context={
        'students':Student.objects.all()
    }
    return render(request, 'first_app/new_index.html', context)