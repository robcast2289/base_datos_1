from django.shortcuts import render, redirect, get_object_or_404
from library.models import Libro
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Libro

# Create your views here.

def home(request):
    libros = Libro.objects.all()
    return render(request,'index.html',{'libros':libros})

@login_required
def libro(request,book_id):
    libro = get_object_or_404(Libro,pk=book_id)
    return render(request,'libro.html',{'book':libro})


def register(request):
    data = {
        'form':CustomUserCreationForm
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            phone = user_creation_form.cleaned_data['phone']
            tipo = user_creation_form.cleaned_data['tipo']
            user_creation_form.save(phone,tipo)

            user = authenticate(username=user_creation_form.cleaned_data['username'],password=user_creation_form.cleaned_data['password1'])
            login(request,user)

            return redirect('home')

    return render(request,'registration/register.html',data)
