from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Patient(models.Model):
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    retainer = models.CharField(max_length=20, choices=FOLDER_CHOICES, default='Single', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('user',)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Doctor(models.Model):
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, unique=False, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    retainer = models.CharField(max_length=20, choices=FOLDER_CHOICES, default='Single', null=True)
    busy = models.BooleanField(max_length=5, default = False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return "Dr " + str(self.user.last_name)
        except:
            return str(self.id)


class LabScientist(models.Model):
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, unique=False, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    retainer = models.CharField(max_length=20, choices=FOLDER_CHOICES, default='Single', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('user',)
        verbose_name = "Lab Technician"
        verbose_name_plural = "Lab Technicians"

class Nurse(models.Model):
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, unique=False, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    retainer = models.CharField(max_length=20, choices=FOLDER_CHOICES, default='Single', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('user',)

class Pharmacist(models.Model):
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
        ('Dialysis', 'Dialysis'),
        ('Radiology', 'Radiology'),
		('Staff', 'Staff'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, unique=False, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    retainer = models.CharField(max_length=20, choices=FOLDER_CHOICES, default='Single', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('user',)

class Consultation(models.Model):
    appointment = models.ForeignKey('home.Appointment', on_delete = models.SET_NULL,unique = False, null=True)
    patient_symptoms = models.TextField(max_length=255)
    test_result = models.TextField(max_length=255)
    prescription = models.TextField(max_length=255)
    lab_technician = models.ForeignKey(LabScientist, on_delete = models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Patients' History"
        verbose_name_plural = "Patients' Histories"

    def __str__(self):
        return str(self.appointment.patient)
