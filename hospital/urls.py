from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('doctors/', doctors, name='doctors'),
    path('doctors/add/', add_doctor, name='add_doctor'),
    path('doctors/<int:pk>/edit/', edit_doctor, name='edit_doctor'),
    path('doctors/<int:pk>/delete/', delete_doctor, name='delete_doctor'),
    path('patients/', patients, name='patients'),
    path('patients/add/', add_patient, name='add_patient'),
    path('patients/<int:pk>/edit/', edit_patient, name='edit_patient'),
    path('patients/<int:pk>/delete/', delete_patient, name='delete_patient'),
    path('appointments/', appointments, name='appointments'),
    path('appointments/add/', add_appointment, name='add_appointment'),
    path('appointments/<int:pk>/edit/', edit_appointment, name='edit_appointment'),
    path('appointments/<int:pk>/delete/', delete_appointment, name='delete_appointment'),
]
