from django import forms
from .models import Appointment, Doctor, Patient

class ObjectChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.id} - {obj.first_name} {obj.last_name}"

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'illness', 'birthday', 'email', 'phone']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'field', 'email', 'phone']

class AppointmentForm(forms.ModelForm):
    patient = ObjectChoiceField(queryset=Patient.objects.all())
    doctor = ObjectChoiceField(queryset=Doctor.objects.all())

    class Meta:
        model = Appointment
        fields = ['date', 'start_time', 'end_time', 'doctor', 'patient']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }