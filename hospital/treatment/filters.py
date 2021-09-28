import django_filters as filters
from django_filters import CharFilter, DateFilter, ModelChoiceFilter
from .models import Consultation, Patient
from django.forms.widgets import TextInput

class ConsultationFilter(filters.FilterSet):
    patient_symptoms = CharFilter(field_name='patient_symptoms', lookup_expr='icontains', label="Patient's Complaints")
    test_result = CharFilter(field_name='test_result', lookup_expr='icontains', label='Test Result')
    start_date = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='gte', label='Dates Above', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    start_date2 = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='lte', label='Dates Below', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    created = DateFilter(label="Exact Date", input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    class Meta:
        model = Consultation
        fields = ['appointment', 'appointment__patient', 'injection', 'tablet', 'syrup', 'suppository']

    def __init__(self, *args, **kwargs):
        super(ConsultationFilter, self).__init__(*args, **kwargs)
        self.filters['appointment'].label="Appointment ID"
        self.filters['appointment__patient'].label="Patient's Card No"
