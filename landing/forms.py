from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'ciudad', 'marca_interes', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'placeholder': '+51 999 999 999'}),
            'mensaje': forms.Textarea(attrs={
                'placeholder': 'Cuéntanos qué experiencia buscas...',
                'rows': 4,
            }),
        }