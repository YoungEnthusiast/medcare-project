import django_filters as filters
from django_filters import CharFilter, DateFilter
from .models import Injection, Tablet, Syrup, Suppository
from django.forms.widgets import TextInput

class InjectionFilter(filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label="Type")
    price = CharFilter(field_name='price', lookup_expr='icontains', label="Price")
    start_date = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='gte', label='Dates Above', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    start_date2 = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='lte', label='Dates Below', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    created = DateFilter(label="Exact Date", input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))

    class Meta:
        model = Injection
        fields = []

class TabletFilter(filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label="Type")
    price = CharFilter(field_name='price', lookup_expr='icontains', label="Price")
    start_date = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='gte', label='Dates Above', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    start_date2 = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='lte', label='Dates Below', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    created = DateFilter(label="Exact Date", input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))

    class Meta:
        model = Tablet
        fields = []

class SyrupFilter(filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label="Type")
    price = CharFilter(field_name='price', lookup_expr='icontains', label="Price")
    start_date = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='gte', label='Dates Above', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    start_date2 = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='lte', label='Dates Below', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    created = DateFilter(label="Exact Date", input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))

    class Meta:
        model = Syrup
        fields = []

class SuppositoryFilter(filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label="Type")
    price = CharFilter(field_name='price', lookup_expr='icontains', label="Price")
    start_date = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='gte', label='Dates Above', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    start_date2 = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], field_name="created", lookup_expr='lte', label='Dates Below', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))
    created = DateFilter(label="Exact Date", input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Format: 1-1-2021 or 1/1/2021'}))

    class Meta:
        model = Suppository
        fields = []
