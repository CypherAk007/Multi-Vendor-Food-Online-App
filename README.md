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