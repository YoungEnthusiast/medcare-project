from django import forms
from .models import Patient, Doctor, Consultation
from django import forms

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['phone_number', 'blood_group', 'gender', 'address', 'age', 'retainer']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['busy']

class ConsultationForm(forms.ModelForm):
    patient_symptoms = forms.CharField(label="Patient's Complaints", widget=forms.Textarea)
    test_result = forms.CharField(required=False, label='Test Result', widget=forms.Textarea)
    prescription = forms.CharField(required=False, label='Prescription', widget=forms.Textarea)
    class Meta:
        model = Consultation
        fields = ['appointment', 'patient_symptoms', 'test_result', 'prescription']#, 'lab_technician']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['lab_technician'].label = 'Lab Technician'
