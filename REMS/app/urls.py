from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.create_property, name='properties'),
    path('agents/', views.agnets, name='agents'),
    path('appointments/', views.appointments, name='appointments'),
    #path('feedback/', views.feedback_page, name='feedback'),
    #path('login/', views.login_page, name='login'),
    #path('registration/', views.registration_page, name='registration')
]
