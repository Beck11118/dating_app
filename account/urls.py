from django.urls import path
from .views import register, user_login, CustomLogoutView

app_name='account'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]