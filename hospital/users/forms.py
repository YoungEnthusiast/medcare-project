from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    GENDER_CHOICES = [
		('Male','Male'),
		('Female', 'Female')
	]
    RETAINER_CHOICES = [
        ('Private', 'Private'),
		('Family', 'Family'),
    ]
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    blood_group = forms.CharField(max_length=10)
    retainer = forms.ChoiceField(choices=RETAINER_CHOICES)
    phone_number = forms.CharField(label='Phone Number')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    age = forms.IntegerField()
    address = forms.CharField(max_length=200)

    # def clean_email(self):
    #    email = self.cleaned_data.get('email')
    #    if CustomUser.objects.filter(email=email).exists():
    #        raise ValidationError("A user with the supplied email already exists")
    #    return email

    # def clean_username(self):
    #    username = self.cleaned_data.get('username')
    #    if CustomUser.objects.filter(username=username).exists():
    #        raise ValidationError("A user with the supplied username already exists")
    #    return username

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'gender', 'address', 'age', 'blood_group', 'retainer', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = "Email Address"
        self.fields['email'].help_text = "This field is required. It must be a valid email address"
        self.fields['password1'].help_text = "<ul><li>Be rest assured that your password will be encrypted (hidden). That means even the website developer will not be able to see it.</li><li>Your password can’t be too similar to your other personal information.<li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>"
        self.fields['password2'].label = "Password Confirmation"

class ProfileEditForm(UserChangeForm):
    GENDER_CHOICES = [
		('Male','Male'),
		('Female', 'Female')
	]
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'gender', 'address', 'age', 'blood_group', 'retainer', 'password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        #self.fields['email'].label = "Email Address"
