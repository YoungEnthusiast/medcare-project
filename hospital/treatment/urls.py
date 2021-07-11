from django.urls import path
from . import views
from home import views as home_views

urlpatterns = [
    path('doctor-dashboard', views.showDoctorBoard, name='doctor_dashboard'),
    path('doctor-dashboard/patients', views.showPatientsDoc, name='patients_doc'),
    path('doctor-dashboard/appointments/', home_views.showAppointmentsDoc, name='appointments_doc'),
    path('doctor-dashboard/appointments/appointments/update/<int:id>', home_views.updateAppointmentDoc, name='appointment_update'),
    path('doctor-dashboard/appointments/appointments/delete/<int:id>', home_views.deleteAppointmentDoc),
    path('patient/<str:pk>/', views.showPatient, name='show_patient'),
    path('doctor-dashboard/doctor-status', views.showDoctorStatus, name='doctor_status'),
    path('doctor-dashboard/doctor-status/update/<int:id>', views.updateDoctorStatus, name='doctor_status_update'),
    path('doctor-dashboard/patients-histories', views.showConsultationsDoc, name='consultations_doc'),
    path('doctor-dashboard/patients-histories/update/<int:id>', views.updateConsultationDoc, name='update_consultation_doc'),
    path('doctor-dashboard/new-medical-history', views.createConsultation, name='new_history'),
    path('lab-scientist-dashboard', views.showLabScBoard, name='lab_sc_dashboard'),
    path('lab-scientist-dashboard/patients', views.showPatientsLab, name='patients_lab'),
    path('lab-scientist-dashboard/patients-histories', views.showConsultationsLab, name='consultations_lab'),
    path('lab-scientist-dashboard/patients-histories/update/<int:id>', views.updateConsultationLab, name='update_consultation'),
    path('nurse-dashboard', views.showNurseBoard, name='nurse_dashboard'),
    path('nurse-dashboard/patients', views.showPatientsNur, name='patients_nur'),
    path('nurse-dashboard/patients-histories', views.showConsultationsNur, name='consultations_nur'),
    path('pharmacist-dashboard', views.showPharmacistBoard, name='pharmacist_dashboard'),
    path('pharmacist-dashboard/patients', views.showPatientsPha, name='patients_pha'),
    path('pharmacist-dashboard/patients-histories', views.showConsultationsPha, name='consultations_pha'),
]
