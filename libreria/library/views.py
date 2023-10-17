from django.shortcuts import render
from library.models import Libro

# Create your views here.

def home(request):
    libros = Libro.objects.all()
    return render(request,'home.html',{'libros':libros})