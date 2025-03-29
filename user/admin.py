from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')  # Agrega más campos visibles
    list_filter = ('is_staff', 'is_superuser', 'is_active')  # Filtros laterales
    search_fields = ('username', 'email')  # Habilita búsqueda
    ordering = ('-date_joined',)  # Ordena por fecha de creación
    fieldsets = BaseUserAdmin.fieldsets + (  # Agregar más secciones en la vista de edición
        ('Información Extra', {'fields': ('telefono', 'direccion')}),  # Agrega campos personalizados
    )

# Registrar el modelo con la nueva configuración
admin.site.register(User, CustomUserAdmin)
