import django_filters as filters
from django_filters import CharFilter, DateFilter
from .models import Appointment, Invoice
from django.forms.widgets import TextInput

class AppointmentFilter(filters.FilterSet):
    start_date = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='gte', label='Dates Above', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    start_date2 = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='lte', label='Dates Below', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    created = DateFilter(label="Exact Date", input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))

    class Meta:
        model = Appointment
        fields = ['receptionist', 'appointment_Id', 'patient', 'doctor', 'status']

    def __init__(self, *args, **kwargs):
        super(AppointmentFilter, self).__init__(*args, **kwargs)
        self.filters['patient'].label="Patient's Card No"
        self.filters['appointment_Id'].label='Appointment ID'

class InvoiceFilter(filters.FilterSet):
    start_date = DateFilter(field_name="created", lookup_expr='gte', label='Date')

    class Meta:
        model = Invoice
        fields = ['appointment', 'blood_test', 'admission', 'injection', 'medicine', 'confirmation']

    def __init__(self, *args, **kwargs):
        super(InvoiceFilter, self).__init__(*args, **kwargs)
        self.filters['blood_test'].label="Blood Test"
