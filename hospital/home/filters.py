import django_filters as filters
from django_filters import CharFilter, DateFilter
from .models import Appointment, Invoice



class AppointmentFilter(filters.FilterSet):
    start_date = DateFilter(field_name="created", lookup_expr='gte', label='Date')

    class Meta:
        model = Appointment
        fields = ['receptionist', 'appointment_Id', 'patient', 'doctor', 'status']

    def __init__(self, *args, **kwargs):
        super(AppointmentFilter, self).__init__(*args, **kwargs)
        self.filters['patient'].label="Patient's ID"
        self.filters['appointment_Id'].label='Appointment ID'

class InvoiceFilter(filters.FilterSet):
    start_date = DateFilter(field_name="created", lookup_expr='gte', label='Date')

    class Meta:
        model = Invoice
        fields = ['appointment', 'blood_test', 'admission', 'injection', 'medicine', 'confirmation']

    def __init__(self, *args, **kwargs):
        super(InvoiceFilter, self).__init__(*args, **kwargs)
        self.filters['blood_test'].label="Blood Test"
