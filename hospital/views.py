from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from requests import request

from hospital.forms import AppointmentForm, DoctorForm, PatientForm
from hospital.models import Appointment, Doctor, Patient


# Create your views here.
def index(request):
    patients_url = reverse('patients')
    doctors_url = reverse('doctors')
    appointments_url = reverse('appointments')
    context = {
        'patients_url': patients_url,
        'doctors_url': doctors_url,
        'appointments_url': appointments_url
    }
    return render(request, 'index.html', context)

def patients(request):
    patients = Patient.objects.all()
    query = request.GET.get('q')
    if query:
        patients = patients.filter(
            Q(id__icontains=query) | 
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(illness__icontains=query) |
            Q(birthday__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query)
        )
    paginator = Paginator(patients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'patients': page_obj
    }

    return render(request, 'patients/patients.html', context)

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm()

    return render(request, 'patients/patient_form.html', {'form': form})

def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patients/patient_form.html', {'form': form, 'patient': patient})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('patients')
    
def doctors(request):
    doctors = Doctor.objects.all()
    query = request.GET.get('q')
    if query:
        doctors = doctors.filter(
            Q(id__icontains=query) | 
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(field__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query)
        )
    paginator = Paginator(doctors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'doctors': page_obj
    }

    return render(request, 'doctors/doctors.html', context)

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()

    return render(request, 'doctors/doctor_form.html', {'form': form})

def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'doctors/doctor_form.html', {'form': form, 'doctor': doctor})

def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return redirect('doctors')

def appointments(request):
    appointments = Appointment.objects.all()
    query = request.GET.get('q')
    if query:
        appointments = appointments.filter(
            Q(id__icontains=query) | 
            Q(date__icontains=query) | 
            Q(start_time__icontains=query) |
            Q(end_time__icontains=query)
        )
    paginator = Paginator(appointments, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'appointments': page_obj
    }

    return render(request, 'appointments/appointments.html', context)

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/appointment_form.html', {'form': form})

def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'appointments/appointment_form.html', {'form': form, 'appointment': appointment})

def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return redirect('appointments')
