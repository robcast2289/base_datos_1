from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from library.models import Usuario, TipoUsuario, Pretamo
from django.db import transaction
from datetime import datetime as datetimeNow
import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy

class CustomUserCreationForm(UserCreationForm):

    phone = forms.CharField(max_length=8)
    tipo = forms.ModelChoiceField(queryset=TipoUsuario.objects.all(),required=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','phone','tipo','password1','password2']

    @transaction.atomic
    def save(self,phone,tipo):
        user = super().save(commit=False)
        user.save()
        Usuario.objects.create(user=user,phone=phone,tipo=tipo)

        return user
    

class PrestamoForm(forms.ModelForm):

    """ def __init__(self,*args,**kwargs):
        super(PrestamoForm).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse_lazy('')
        self.helper.form_method = 'post' """

    fecha_prestamo = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local','min':datetimeNow.now().date()}))
    fecha_devolucion = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local','min':datetimeNow.now().date()}))
    #fecha_devolucion = forms.DateTimeField(initial=datetime.date.today)
    class Meta:
        model = Pretamo
        fields = ['fecha_prestamo','fecha_devolucion']

    @transaction.atomic
    def save(self,user,libro):
        prestamo = super().save(commit=False)
        prestamo.user = user
        prestamo.libro = libro
        prestamo.save()

        return prestamo