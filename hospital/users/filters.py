import django_filters as filters
from django_filters import CharFilter, DateFilter, ModelChoiceFilter
#from .models import AdaptedUser
from treatment.models import Patient

class PatientFilter(filters.FilterSet):
    start_date = DateFilter(field_name="created", lookup_expr='gte', label='Date')

    class Meta:
        model = Patient
        fields = ['user__username', 'user__first_name', 'user__last_name', 'retainer']

    def __init__(self, *args, **kwargs):
        super(PatientFilter, self).__init__(*args, **kwargs)
        self.filters['user__username'].label="ID"
        self.filters['user__first_name'].label="First Name"
        self.filters['user__last_name'].label="Last Name"
