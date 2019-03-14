from django.apps import AppConfig


class LoginAppConfig(AppConfig):
    name = 'Login_app'

    def ready(self):
        import Login_app.signals
