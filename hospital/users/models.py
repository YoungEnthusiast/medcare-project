from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
		('Male','Male'),
		('Female', 'Female')
	]
    RETAINER_CHOICES = [
        ('Private', 'Private'),
		('Family', 'Family'),
    ]
    phone_number = models.CharField(max_length=20, unique=False, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    retainer = models.CharField(max_length=20, choices=RETAINER_CHOICES, default='Private', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Person'
        verbose_name_plural = 'People'
