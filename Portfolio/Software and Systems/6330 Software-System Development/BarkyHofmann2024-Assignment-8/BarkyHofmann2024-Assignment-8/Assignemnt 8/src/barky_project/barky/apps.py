from django.apps import AppConfig


class BarkyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'barky'

    def ready(self):
        import barky.signals
