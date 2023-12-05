from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.create_property, name='properties'),
    path('agents/', views.agnets, name='agents'),
    path('appointments/', views.appointments, name='appointments'),
    path('feedback/', views.feedback, name='feedback'),
    path('', views.home, name='index'),
    path('login/',views.login, name='login')
]
