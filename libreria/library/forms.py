from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from library.models import Usuario, TipoUsuario
from django.db import transaction

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