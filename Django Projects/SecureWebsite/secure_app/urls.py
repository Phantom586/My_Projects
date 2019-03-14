from django.urls import path
from secure_app import views

app_name = 'secure_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]