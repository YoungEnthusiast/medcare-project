import django_filters as filters
from django_filters import CharFilter, DateFilter
from .models import Injection, Tablet, Syrup, Suppository

class InjectionFilter(filters.FilterSet):
    created = DateFilter(field_name="created", lookup_expr='gte', label='Date')
    price = CharFilter(field_name='price', lookup_expr='icontains', label="Price")

    class Meta:
        model = Injection
        fields = ['created', 'name', 'price']

    def __init__(self, *args, **kwargs):
        super(InjectionFilter, self).__init__(*args, **kwargs)
        self.filters['created'].label="Date"
        self.filters['name'].label="Type"

class TabletFilter(filters.FilterSet):
    created = DateFilter(field_name="created", lookup_expr='gte', label='Date')
    price = CharFilter(field_name='price', lookup_expr='icontains', label="Price")

    class Meta:
        model = Tablet
        fields = ['created', 'name', 'price']

    def __init__(self, *args, **kwargs):
        super(TabletFilter, self).__init__(*args, **kwargs)
        self.filters['created'].label="Date"
        self.filters['name'].label="Type"

class SyrupFilter(filters.FilterSet):
    created = DateFilter(field_name="created", lookup_expr='gte', label='Date')
    price = CharFilter(field_name='price', lookup_expr='icontains', label="Price")

    class Meta:
        model = Syrup
        fields = ['created', 'name', 'price']

    def __init__(self, *args, **kwargs):
        super(SyrupFilter, self).__init__(*args, **kwargs)
        self.filters['created'].label="Date"
        self.filters['name'].label="Type"

class SuppositoryFilter(filters.FilterSet):
    created = DateFilter(field_name="created", lookup_expr='gte', label='Date')
    price = CharFilter(field_name='price', lookup_expr='icontains', label="Price")

    class Meta:
        model = Suppository
        fields = ['created', 'name', 'price']

    def __init__(self, *args, **kwargs):
        super(SuppositoryFilter, self).__init__(*args, **kwargs)
        self.filters['created'].label="Date"
        self.filters['name'].label="Type"
