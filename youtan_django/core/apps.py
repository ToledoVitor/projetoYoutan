from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'youtan_django.core'
    verbose_name = 'core models'

    default_auto_field = 'django.db.models.BigAutoField'
