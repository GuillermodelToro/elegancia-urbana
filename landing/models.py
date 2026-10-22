from django.db import models


class Contacto(models.Model):
    CIUDADES = [
        ('lima', 'Lima'),
        ('bogota', 'Bogotá'),
        ('cdmx', 'Ciudad de México'),
    ]

    MARCAS = [
        ('louis_vuitton', 'Louis Vuitton'),
        ('gucci', 'Gucci'),
        ('chanel', 'Chanel'),
    ]

    nombre = models.CharField('Nombre completo', max_length=100)
    email = models.EmailField('Correo electrónico')
    telefono = models.CharField('Teléfono', max_length=20, blank=True)
    ciudad = models.CharField('Ciudad', max_length=20, choices=CIUDADES)
    marca_interes = models.CharField('Marca de interés', max_length=20, choices=MARCAS)
    mensaje = models.TextField('Mensaje')
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f'{self.nombre} - {self.email}'