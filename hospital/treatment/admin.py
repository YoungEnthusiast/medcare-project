from django.contrib import admin
from .models import Patient, Doctor, Consultation, LabScientist, Pharmacist, Nurse

class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    list_per_page = 10

admin.site.register(Patient, PatientAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'busy']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'busy']
    list_filter = ['busy']
    list_editable = ['busy']
    list_per_page = 10

class LabScientistAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    list_per_page = 10

class NurseAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    list_per_page = 10

class PharmacistAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    list_per_page = 10

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['created', 'appointment', 'patient_symptoms', 'test_result', 'injection']
    search_fields = ['doctor__username', 'doctor__first_name', 'user__last_name', 'patient__username']
    #list_filter = ['status']
    list_display_links = ['appointment']
    list_per_page = 10

    def patient(self, obj):
        return obj.appointment.patient
        patient.admin_order_field = appointment
        get_patient.short_description = Patient

    def doctor(self, obj):
        return obj.appointment.doctor
        doctor.admin_order_field = appointment
        get_doctor.short_description = Doctor

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(LabScientist, LabScientistAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(Pharmacist, PharmacistAdmin)
admin.site.register(Consultation, ConsultationAdmin)
