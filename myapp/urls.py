from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('loginpage/', views.login),
    path('form/', views.form),
    path('words/', views.words),
]