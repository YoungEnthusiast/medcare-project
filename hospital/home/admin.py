from django.contrib import admin
from .models import Contact, Receptionist, Appointment, Invoice, HR

class ContactAdmin(admin.ModelAdmin):
    list_display = ['date_submitted', 'name', 'email', 'phone_number', 'message', 'status']
    search_fields = ['date_submitted', 'name', 'email' 'phone_number', 'status']
    list_filter = ['status']
    list_editable = ['status']
    list_display_links = ['name', 'email']
    list_per_page = 10

class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user__identifier', 'user__first_name', 'user__last_name']
    list_per_page = 10

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['created', 'receptionist', 'appointment_Id', 'patient', 'doctor', 'status']
    search_fields = ['appointment_Id', 'receptionist', 'doctor', 'patient']
    list_filter = ['status', 'receptionist']
    list_editable = ['status']
    list_display_links = ['appointment_Id']
    list_per_page = 10

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['created', 'receptionist', 'appointment', 'blood_test', 'admission', 'injection', 'medicine', 'total', 'confirmation', 'updated']
    search_fields = ['appointment__appointment_Id', 'receptionist', 'blood_test', 'admission', 'injection', 'medicine', 'confirmation']
    list_filter = ['confirmation', 'receptionist']
    list_editable = ['confirmation']
    list_display_links = ['appointment']
    list_per_page = 10

class HRAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user_identifier']
    list_per_page = 10

admin.site.register(Contact, ContactAdmin)
admin.site.register(Receptionist, ReceptionistAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(HR, HRAdmin)
