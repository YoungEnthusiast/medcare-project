from django import forms
from .models import Doctor, Consultation
from users.models import CustomUser

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['busy']

class ConsultationForm(forms.ModelForm):
    patient_symptoms = forms.CharField(label='Patient Symptoms', widget=forms.Textarea)
    test_result = forms.CharField(required=False, label='Test Result', widget=forms.Textarea)
    prescription = forms.CharField(required=False, label='Prescription', widget=forms.Textarea)
    class Meta:
        model = Consultation
        fields = ['appointment', 'patient_symptoms', 'test_result', 'prescription']
