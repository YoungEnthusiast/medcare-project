import django_filters as filters
from django_filters import CharFilter, DateFilter, ModelChoiceFilter
from .models import Consultation, Patient

class ConsultationFilter(filters.FilterSet):
    start_date = DateFilter(field_name="created", lookup_expr='gte', label='Date')
    patient_symptoms = CharFilter(field_name='patient_symptoms', lookup_expr='icontains', label='Symptoms')
    test_result = CharFilter(field_name='test_result', lookup_expr='icontains', label='Test Result')
    Prescription = CharFilter(field_name='prescription', lookup_expr='icontains', label='Prescription')

    class Meta:
        model = Consultation
        fields = ['appointment', 'appointment__patient']

    def __init__(self, *args, **kwargs):
        super(ConsultationFilter, self).__init__(*args, **kwargs)
        self.filters['appointment'].label="Appointment ID"
        self.filters['appointment__patient'].label="Patient's ID"
