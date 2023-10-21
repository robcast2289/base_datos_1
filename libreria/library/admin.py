from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from library.models import *

# Register your models here.

class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = "Usuarios"


class UserAdmin(BaseUserAdmin):
    inlines = [UsuarioInline]



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(TipoUsuario)
admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Pretamo)
