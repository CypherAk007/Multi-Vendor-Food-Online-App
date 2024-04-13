## Multi Vendor App - Django

### Create Django Proj
- django-admin startproject foodOnline_main .
- here . represents cur dir level

### Configure Templates for Django to ref frontend from templates folder
- 'DIRS': ['templates'],
- ![Alt text](readme_images/templates.png)

### Configure static folder and static floder path
- STATIC_ROOT = BASE_DIR /'static'
- STATICFILES_DIRS = [
    'foodOnline_main/static'
]

### For every page you want static files then add this in that file
- {% load static %}
- To load css from static folder  - 	<link href="{% static 'css/iconmoon.css'%}" rel="stylesheet">
