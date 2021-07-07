#For views.py
#from django.conf import settings
#User = settings.AUTH_USER_MODEL
from django.db import models
from users.models import CustomUser

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.user.identifier)

    class Meta:
        ordering = ('user',)

class Doctor(models.Model):
    user  = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)
    busy = models.BooleanField(max_length=5, default = False)

    def __str__(self):
        return "Dr " + str(self.user.last_name)

class LabScientist(models.Model):
    user  = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.user.last_name)

    class Meta:
        ordering = ('user',)
        verbose_name = "Lab Technician"
        verbose_name_plural = "Lab Technicians"

class Nurse(models.Model):
    user  = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.user.last_name)

class Pharmacist(models.Model):
    user  = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.user.last_name)

class Consultation(models.Model):
    appointment = models.ForeignKey('home.Appointment', on_delete = models.SET_NULL,unique = False, null=True)
    patient_symptoms = models.TextField(max_length=255)
    test_result = models.TextField(max_length=255)
    prescription = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Patients' History"
        verbose_name_plural = "Patients' Histories"

    # def __str__(self):
    #     return str(self.appointment.patient)
