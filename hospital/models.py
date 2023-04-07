from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    illness = models.CharField(max_length=20)
    birthday = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    field = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Appointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
