from django.urls import path
from . import views
from home import views as home_views

urlpatterns = [
    path('doctor-dashboard', views.showDoctorBoard, name='doctor_dashboard'),
    path('doctor-dashboard/patients', views.showPatients, name='patients_doc'),
    path('doctor-dashboard/appointments/', home_views.showAppointments, name='appointments_doc'),
    path('doctor-dashboard/appointments/update/<int:id>', home_views.updateAppointment, name='appointment_update'),
    path('doctor-dashboard/appointments/delete/<int:id>', home_views.deleteAppointment),
    path('patient/<str:pk>/', views.showPatient, name='show_patient'),
    path('doctor-dashboard/doctor-status', views.showDoctorStatus, name='doctor_status'),
    path('doctor-dashboard/doctor-status/update/<int:id>', views.updateDoctorStatus, name='doctor_status_update'),
    path('doctor-dashboard/patients-histories', views.showConsultations, name='consultations'),
    path('doctor-dashboard/patients-histories/update/<int:id>', views.updateConsultation, name='update_consultation'),
    path('doctor-dashboard/new-medical-history', views.createConsultation, name='new_history'),
    path('lab-scientist-dashboard', views.showLabScBoard, name='lab_sc_dashboard'),
    path('lab-scientist-dashboard/patients', views.showPatients, name='patients_lab'),
    path('lab-scientist-dashboard/patients-histories', views.showConsultations, name='consultations_lab'),
    path('lab-scientist-dashboard/patients-histories/update/<int:id>', views.updateConsultationLab, name='update_consultation'),
    path('nurse-dashboard', views.showNurseBoard, name='nurse_dashboard'),
    path('nurse-dashboard/patients', views.showPatients, name='patients_nur'),
    path('nurse-dashboard/patients-histories', views.showConsultations, name='consultations_nur'),
    path('pharmacist-dashboard', views.showPharmacistBoard, name='pharmacist_dashboard'),
    path('pharmacist-dashboard/patients', views.showPatients, name='patients_pha'),
    path('pharmacist-dashboard/patients-histories', views.showConsultations, name='consultations_pha'),

]
