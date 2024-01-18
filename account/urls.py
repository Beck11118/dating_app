from django.urls import path
from .views import register, user_login

app_name='account'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]