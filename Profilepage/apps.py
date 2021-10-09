from django.apps import AppConfig


class ProfilepageConfig(AppConfig):
    name = 'Profilepage'


    def ready(self):
        import Profilepage.signals
