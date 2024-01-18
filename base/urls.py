from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('matches/', views.match_view, name='match_view'),
    path('message/<str:receiver_username>/', views.message_view, name='message_view'),
]