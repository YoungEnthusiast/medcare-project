import django_filters as filters
from django_filters import CharFilter, DateFilter, ModelChoiceFilter
#from .models import CustomUser
from treatment.models import Patient

class PatientFilter(filters.FilterSet):
    start_date = DateFilter(field_name="created", lookup_expr='gte', label='Date')

    class Meta:
        model = Patient
        fields = ['user__identifier', 'user__first_name', 'user__last_name', 'user__retainer']

    def __init__(self, *args, **kwargs):
        super(PatientFilter, self).__init__(*args, **kwargs)
        self.filters['user__identifier'].label="ID"
        self.filters['user__first_name'].label="First Name"
        self.filters['user__last_name'].label="Last Name"
        self.filters['user__retainer'].label="Retainer"
