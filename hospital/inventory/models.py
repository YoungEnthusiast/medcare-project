from django.db import models

class Injection(models.Model):
    name = models.CharField(max_length=30, null=True)
    price = models.IntegerField(blank=True, default = 0, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        # verbose_name = "Patients' History"
        # verbose_name_plural = "Patients' Histories"

    def __str__(self):
        return str(self.name)

class Tablet(models.Model):
    name = models.CharField(max_length=30, null=True)
    price = models.IntegerField(blank=True, default = 0, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        # verbose_name = "Patients' History"
        # verbose_name_plural = "Patients' Histories"

    def __str__(self):
        return str(self.name)

    # @property
    # def myPrice(self):
    #     if self.price == None:
    #         return 0

class Syrup(models.Model):
    name = models.CharField(max_length=30, null=True)
    price = models.IntegerField(blank=True, default = 0, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        # verbose_name = "Patients' History"
        # verbose_name_plural = "Patients' Histories"

    def __str__(self):
        return str(self.name)

class Suppository(models.Model):
    name = models.CharField(max_length=30, null=True)
    price = models.IntegerField(blank=True, default = 0, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Suppository"
        verbose_name_plural = "Suppositories"

    def __str__(self):
        return str(self.name)
