from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Person
from django.core.exceptions import ValidationError

class CustomRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)

    # def clean_email(self):
    #    email = self.cleaned_data.get('email')
    #    if User.objects.filter(email=email).exists():
    #        raise ValidationError("A user with the supplied email already exists")
    #    return email

    def clean_username(self):
       username = self.cleaned_data.get('username')
       if User.objects.filter(username=username).exists():
           raise ValidationError("A user with the supplied username already exists")
       return username

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['username'].label = 'ID (Username)'
        self.fields['email'].help_text = "This field must be a valid email address"
        self.fields['password1'].help_text = "<ul><li>Be rest assured that your password will be encrypted (hidden). That means even the website developer will not be able to see it.</li><li>Your password can’t be too similar to your other personal information.<li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>"
        self.fields['password2'].label = "Password Confirmation"

class UserEditForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"

class PersonEditForm(forms.ModelForm):
    GENDER_CHOICES = [
		('Male','Male'),
		('Female', 'Female')
	]
    FOLDER_CHOICES = [
        ('Single', 'Single'),
		('Family', 'Family'),
        ('NHIS', 'NHIS'),
		('HMO', 'HMO'),
        ('Dental', 'Dental'),
		('OPD', 'OPD'),
        ('ANC', 'ANC'),
		('Staff', 'Staff'),
    ]
    ROLE_CHOICES = [
        ('Patient', 'Patient'),
        ('Front Desk Officer', 'Front Desk Officer'),
		('Doctor', 'Doctor'),
        ('Lab Technician', 'Lab Technician'),
        ('Nurse', 'Nurse'),
		('Pharmacist', 'Pharmacist'),
        ('Admin', 'Admin')
    ]
    # first_name = forms.CharField(max_length=30)
    # last_name = forms.CharField(max_length=30)
    # email = forms.EmailField()
    # username = forms.CharField(max_length=20)
    blood_group = forms.CharField(required=False, max_length=10)
    retainer= forms.ChoiceField(choices=FOLDER_CHOICES)
    phone_number = forms.CharField(label='Phone Number')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    age = forms.IntegerField()
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    address = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Person
        fields = ['phone_number', 'blood_group', 'gender', 'address', 'age', 'retainer', 'role']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].help_text = "Phone Number"
        self.fields['blood_group'].label = "Blood Group"
        self.fields['retainer'].label = "Folder Type"
        self.fields['role'].label = "Department"
