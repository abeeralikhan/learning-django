from django.apps import AppConfig


class MyComponentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_component'
