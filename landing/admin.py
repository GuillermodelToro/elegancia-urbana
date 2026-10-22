from django.contrib import admin
from .models import Contacto


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'ciudad', 'marca_interes', 'fecha_registro')
    list_filter = ('ciudad', 'marca_interes', 'fecha_registro')
    search_fields = ('nombre', 'email')