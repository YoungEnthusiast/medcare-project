from django import forms
from .models import Injection, Tablet, Syrup, Suppository

class InjectionForm(forms.ModelForm):
    class Meta:
        model = Injection
        fields = ['name', 'price']

class TabletForm(forms.ModelForm):
    class Meta:
        model = Tablet
        fields = ['name', 'price']

class SyrupForm(forms.ModelForm):
    class Meta:
        model = Syrup
        fields = ['name', 'price']

class SuppositoryForm(forms.ModelForm):
    class Meta:
        model = Suppository
        fields = ['name', 'price']
