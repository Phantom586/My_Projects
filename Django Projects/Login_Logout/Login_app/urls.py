from django.urls import path
from django.contrib.auth import views as auth_views
from Login_app import views

app_name = 'Login_app'

urlpatterns = [
    # path('Sign_In/', views.signin, name='signin'),
    path('Register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='Login_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Login_app/logout.html'), name='logout'),
    path('Show_Database/', views.show_database, name='show_database'),
]