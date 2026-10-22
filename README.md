# Elegancia Urbana | Landing Page en Django

Landing page profesional y responsiva para la startup de moda de lujo **Elegancia Urbana**, desarrollada con Django (patrón MTV), HTML5 y CSS3, servida desde Linux Fedora.

## Tecnologías
- Python 3.14 y Django 6.1
- HTML5 semántico y plantillas de Django
- CSS3 (variables, Flexbox, Grid y media queries)
- SQLite como base de datos
- Linux Fedora (servidor) y Visual Studio Code con Remote-SSH (editor)

## Estructura MTV
- **Model:** `landing/models.py`, modelo `Contacto` que guarda los datos del formulario.
- **Template:** `landing/templates/landing/base.html` e `index.html`.
- **View:** `landing/views.py`, vista `inicio` que muestra el landing y procesa el formulario.

## Secciones
1. Información de la empresa
2. Catálogo de marcas (Louis Vuitton, Gucci, Chanel)
3. Servicios premium
4. Ciudades donde opera (Lima, Bogotá, Ciudad de México)
5. Formulario de contacto funcional

## Instalación
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

Sitio: `http://<IP-del-servidor>:8000`
Panel de administración: `http://<IP-del-servidor>:8000/admin`