from django import forms
from .models import Contact, Appointment, Invoice

class ContactForm(forms.ModelForm):
    phone_number = forms.CharField(label='Phone Number')
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'status']

class InvoiceForm(forms.ModelForm):
    blood_test = forms.IntegerField(required=False, label='Blood Test')
    admission = forms.IntegerField(required=False, label='Admission')
    injection = forms.IntegerField(required=False, label='Injection')
    medicine = forms.IntegerField(required=False, label='Medicine')

    class Meta:
        model = Invoice
        fields = ['receptionist', 'appointment', 'blood_test', 'admission', 'injection', 'medicine', 'confirmation', 'admin']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['blood_test'].label = 'Blood Test'
