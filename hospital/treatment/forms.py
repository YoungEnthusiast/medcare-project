from django import forms
from .models import Patient, Doctor, Consultation
from django.forms.widgets import NumberInput

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
    created = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Consultation
        fields = ['appointment', 'patient_symptoms', 'lab_technician', 'test_result', 'injection', 'injection_dosage', 'injection_how', 'tablet',  'tablet_dosage', 'tablet_how', 'syrup', 'syrup_dosage', 'syrup_how', 'suppository', 'suppository_dosage', 'suppository_how', 'created']

    def __init__(self, *args, **kwargs):
        super(ConsultationForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['patient_symptoms'].required = False
            self.fields['patient_symptoms'].widget.attrs['disabled'] = 'disabled'
            self.fields['test_result'].required = False
            self.fields['test_result'].widget.attrs['disabled'] = 'disabled'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created'].label = 'Date'
class ConsultationFormDoc(forms.ModelForm):
    patient_symptoms = forms.CharField(label="Patient's Complaints", widget=forms.Textarea)
    test_result = forms.CharField(required=False, label='Test Result', widget=forms.Textarea)
    class Meta:
        model = Consultation
        fields = ['appointment', 'patient_symptoms', 'lab_technician', 'test_result', 'injection', 'injection_dosage', 'injection_how', 'tablet',  'tablet_dosage', 'tablet_how', 'syrup', 'syrup_dosage', 'syrup_how', 'suppository', 'suppository_dosage', 'suppository_how']

    def __init__(self, *args, **kwargs):
        super(ConsultationFormDoc, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['appointment'].required = False
            self.fields['appointment'].widget.attrs['disabled'] = 'disabled'
            self.fields['patient_symptoms'].required = False
            self.fields['patient_symptoms'].widget.attrs['disabled'] = 'disabled'
            self.fields['lab_technician'].required = False
            self.fields['lab_technician'].widget.attrs['disabled'] = 'disabled'
            self.fields['test_result'].required = False
            self.fields['test_result'].widget.attrs['disabled'] = 'disabled'

    def clean_appointment(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.appointment
        else:
            return self.cleaned_data.get('appointment', None)

    def clean_patient_symptoms(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.patient_symptoms
        else:
            return self.cleaned_data.get('patient_symptoms', None)

    def clean_lab_technician(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.lab_technician
        else:
            return self.cleaned_data.get('lab_technician', None)

    def clean_test_result(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.test_result
        else:
            return self.cleaned_data.get('test_result', None)
