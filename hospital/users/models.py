from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Person(models.Model):
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
        ('Receptionist', 'Receptionist'),
		('Doctor', 'Doctor'),
        ('Lab Technician', 'Lab Technician'),
        ('Nurse', 'Nurse'),
		('Pharmacist', 'Pharmacist'),
        ('Admin', 'Admin')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, unique=False, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    retainer = models.CharField(max_length=20, choices=FOLDER_CHOICES, default='Single', null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Patient', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Person.objects.create(user=instance)
            instance.person.save()

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
