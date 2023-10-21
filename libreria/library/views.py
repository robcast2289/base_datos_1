from django.shortcuts import render, redirect, get_object_or_404
from library.models import Libro
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import  login_required
from .forms import CustomUserCreationForm, PrestamoForm
from .models import Libro, Pretamo

# Create your views here.

def home(request):
    print("usuario")
    print(request.user.id)
    if not request.user.id is None:
        libros = Libro.objects.extra(where=[f"""
        NOT EXISTS (select 1 from library_pretamo where library_pretamo.libro_id = library_libro.id and library_pretamo.user_id = {request.user.id} and library_pretamo.fecha_devolucion_real is null)
        """])
    else:
        libros = Libro.objects.all()
    return render(request,'index.html',{'libros':libros})

@login_required
def libro(request,book_id):
    libro = get_object_or_404(Libro,pk=book_id)
    data = {
        'book':libro,
        'form':PrestamoForm
    }
    print(request.user.username)
    if request.method == 'POST':
        print("isPost")
        prestamo_form = PrestamoForm(data=request.POST)

        if prestamo_form.is_valid():
            print("isValid")
            libro = Libro.objects.get(pk=book_id)

            if libro.ejemplares > 0:
                prestamo_form.save(request.user,libro)

                libro.ejemplares = libro.ejemplares - 1
                libro.save()

                return redirect('home')
            else:
                messages.error(request,"No hay libros disponiples para prestar")

    return render(request,'libro.html',data)

@login_required
def prestamo(request):
    prestamo = Pretamo.objects.filter(user=request.user)
    data = {
        'prestamos':prestamo,
    }
    return render(request,'prestamo.html',data)


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
