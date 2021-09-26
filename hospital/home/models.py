from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from treatment.models import Patient, Doctor

class Contact(models.Model):
    STATUS_CHOICES = [
        ('Treated','Treated'),
        ('New', 'New'),
        ('Pending', 'Pending')
    ]
    name = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(max_length=500, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='New', null=True)

    class Meta:
        ordering = ('-date_submitted',)
        verbose_name = 'Contact us Message'
        verbose_name_plural = 'Contact us Messages'

    def __str__(self):
        return str(self.name)

class Receptionist(models.Model):
    GENDER_CHOICES = [
		('Male','Male'),
		('Female', 'Female')
	]
    RETAINER_CHOICES = [
        ('Private', 'Private'),
		('Family', 'Family'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, unique=False, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    retainer = models.CharField(max_length=20, choices=RETAINER_CHOICES, default='Private', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('user',)
class Appointment(models.Model):
    receptionist = models.CharField(max_length=15, blank=True, null=True)
    appointment_Id = models.CharField(
		 max_length = 8,
		 null=True,
		 editable=True,
		 default=2021
	)
    doctor = models.ForeignKey(Doctor, on_delete = models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete = models.SET_NULL, null=True)
    created = models.DateField(null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(max_length =5, default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.appointment_Id)

class HR(models.Model):
    GENDER_CHOICES = [
		('Male','Male'),
		('Female', 'Female')
	]
    RETAINER_CHOICES = [
        ('Private', 'Private'),
		('Family', 'Family'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, unique=False, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    retainer = models.CharField(max_length=20, choices=RETAINER_CHOICES, default='Private', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('user',)

    class Meta:
        ordering = ('user',)
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

class Invoice(models.Model):
    receptionist = models.ForeignKey(Receptionist, on_delete = models.SET_NULL, null=True)
    admin = models.ForeignKey(HR, on_delete = models.SET_NULL, null=True, blank=True)
    appointment = models.ForeignKey(Appointment, on_delete = models.SET_NULL, unique = False, null=True)
    blood_test = models.IntegerField(null=True, default=0)
    admission = models.IntegerField(null=True, default=0)
    injection = models.IntegerField(null=True, default=0)
    medicine = models.IntegerField(null=True, default=0)
    created = models.DateTimeField(null=True, verbose_name="Date")
    updated = models.DateTimeField(auto_now=True, null=True)
    confirmation = models.BooleanField(max_length =5, default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.appointment)

    def total(self):
        if self.blood_test == None and self.admission != None and self.injection != None and self.medicine !=None:
            return self.admission + self.injection + self.medicine
        elif self.admission == None and self.blood_test != None and self.injection != None and self.medicine !=None:
            return self.blood_test + self.injection + self.medicine
        elif self.injection == None and self.blood_test != None and self.admission != None and self.medicine !=None:
            return self.blood_test + self.admission + self.medicine
        elif self.medicine == None and self.blood_test != None and self.admission != None and self.injection !=None:
            return self.blood_test + self.admission + self.injection
        elif self.blood_test == None and self.admission == None and self.injection != None and self.medicine !=None:
            return self.injection + self.medicine
        elif self.blood_test == None and self.injection == None and self.admission != None and self.medicine !=None:
            return self.admission + self.medicine
        elif self.blood_test == None and self.medicine == None and self.injection != None and self.admission !=None:
            return self.injection + self.admission
        elif self.admission == None and self.injection == None and self.blood_test != None and self.medicine !=None:
            return self.blood_test + self.medicine
        elif self.admission == None and self.medicine == None and self.blood_test != None and self.injection != None:
            return self.blood_test + self.injection
        elif self.injection == None and self.medicine == None and self.blood_test != None and self.admission != None:
            return self.blood_test + self.admission
        elif self.blood_test == None and self.admission == None and self.injection == None and self.medicine != None:
            return self.medicine
        elif self.blood_test == None and self.admission != None and self.injection == None and self.medicine == None:
            return self.admission
        elif self.blood_test == None and self.admission == None and self.injection != None and self.medicine == None:
            return self.injection
        elif self.blood_test != None and self.admission == None and self.injection == None and self.medicine == None:
            return self.blood_test
        elif self.blood_test != None and self.admission != None and self.injection != None and self.medicine !=None:
            return self.blood_test + self.admission + self.injection + self.medicine
