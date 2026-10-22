from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ContactoForm


def inicio(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                '¡Gracias! Un asesor de Elegancia Urbana se comunicará contigo muy pronto.'
            )
            return redirect(reverse('landing:inicio') + '#contacto')
    else:
        form = ContactoForm()

    marcas = [
        {
            'nombre': 'Louis Vuitton',
            'descripcion': 'Marroquinería icónica, equipaje de viaje y accesorios de diseño atemporal.',
        },
        {
            'nombre': 'Gucci',
            'descripcion': 'Moda contemporánea con identidad audaz: prendas, calzado y accesorios.',
        },
        {
            'nombre': 'Chanel',
            'descripcion': 'Elegancia clásica en alta costura, bolsos emblemáticos y joyería fina.',
        },
    ]

    servicios = [
        {
            'icono': '✦',
            'titulo': 'Asesoría de imagen personalizada',
            'descripcion': 'Un estilista dedicado analiza tu estilo y te propone looks a tu medida.',
        },
        {
            'icono': '◆',
            'titulo': 'Personal shopper',
            'descripcion': 'Seleccionamos y reservamos las piezas que buscas antes de tu visita.',
        },
        {
            'icono': '❖',
            'titulo': 'Experiencias VIP privadas',
            'descripcion': 'Sesiones exclusivas en sala privada con champán y atención uno a uno.',
        },
        {
            'icono': '✧',
            'titulo': 'Entrega premium a domicilio',
            'descripcion': 'Llevamos tus compras con empaque de lujo hasta la puerta de tu casa.',
        },
    ]

    ciudades = [
        {'nombre': 'Lima', 'pais': 'Perú', 'zona': 'San Isidro'},
        {'nombre': 'Bogotá', 'pais': 'Colombia', 'zona': 'Zona T'},
        {'nombre': 'Ciudad de México', 'pais': 'México', 'zona': 'Polanco'},
    ]

    contexto = {
        'form': form,
        'marcas': marcas,
        'servicios': servicios,
        'ciudades': ciudades,
    }
    return render(request, 'landing/index.html', contexto)