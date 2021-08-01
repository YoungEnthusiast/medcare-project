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
    DOSAGE_CHOICES = [
        ('ods', 'ods'),
		('bd', 'bd'),
        ('tds', 'tds'),
		('wkly', 'wkly'),
        ('monthly', 'monthly'),
    ]
    HOW_CHOICES = [
        ('1', '1'),
		('2', '2'),
        ('3', '3'),
		('4', '4'),
        ('5', '5'),
		('6', '6'),
        ('7', '7'),
		('8', '8'),
        ('9', '9'),
		('10', '10'),
        ('11', '11'),
		('12', '12'),
        ('13', '13'),
		('14', '14'),
        ('15', '15'),
		('16', '16'),
        ('17', '17'),
		('18', '18'),
        ('19', '19'),
		('20', '20'),
        ('21', '21'),
		('22', '22'),
        ('23', '23'),
		('24', '24'),
        ('25', '25'),
		('26', '26'),
        ('27', '27'),
		('28', '28'),
        ('29', '29'),
		('30', '30'),
    ]
    appointment = models.ForeignKey('home.Appointment', on_delete = models.SET_NULL,unique = False, null=True)
    patient_symptoms = models.TextField(max_length=255)
    test_result = models.TextField(max_length=255)
    injection = models.ForeignKey('inventory.Injection', on_delete = models.SET_NULL,unique = False, null=True, blank=True)
    injection_dosage = models.CharField(max_length=7, choices=DOSAGE_CHOICES, default='ods', null=True, blank=True, verbose_name="Injection Dosage")
    injection_how = models.CharField(max_length=3, choices=HOW_CHOICES, default='1', null=True, blank=True, verbose_name="How Long?")
    tablet = models.ForeignKey('inventory.Tablet', on_delete = models.SET_NULL,unique = False, null=True, blank=True)
    tablet_dosage = models.CharField(max_length=7, choices=DOSAGE_CHOICES, default='ods', null=True, blank=True, verbose_name="Tablet Dosage")
    tablet_how = models.CharField(max_length=3, choices=HOW_CHOICES, default='1', null=True, blank=True, verbose_name="How Long?")
    syrup = models.ForeignKey('inventory.Syrup', on_delete = models.SET_NULL,unique = False, null=True, blank=True)
    syrup_dosage = models.CharField(max_length=7, choices=DOSAGE_CHOICES, default='ods', null=True, blank=True, verbose_name="Syrup Dosage")
    syrup_how = models.CharField(max_length=3, choices=HOW_CHOICES, default='1', null=True, blank=True, verbose_name="How Long?")
    suppository = models.ForeignKey('inventory.Suppository', on_delete = models.SET_NULL,unique = False, null=True, blank=True)
    suppository_dosage = models.CharField(max_length=7, choices=DOSAGE_CHOICES, default='ods', null=True, blank=True, verbose_name="Suppository Dosage")
    suppository_how = models.CharField(max_length=3, choices=HOW_CHOICES, default='1', null=True, blank=True, verbose_name="How Long?")
    lab_technician = models.ForeignKey(LabScientist, on_delete = models.SET_NULL, null=True, verbose_name="Lab Technician")
    total = models.IntegerField(blank=True, default = 0, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Patients' History"
        verbose_name_plural = "Patients' Histories"

    def __str__(self):
        try:
            return str(self.appointment.patient)
        except:
            return str(self.id)

    @property
    def myInjection(self):
        if self.injection == None:
            return 0
        else:
            return self.injection.price

    @property
    def myTablet(self):
        if self.tablet == None:
            return 0
        else:
            return self.tablet.price

    @property
    def mySyrup(self):
        if self.syrup == None:
            return 0
        else:
            return self.syrup.price

    @property
    def mySuppository(self):
        if self.suppository == None:
            return 0
        else:
            return self.suppository.price
