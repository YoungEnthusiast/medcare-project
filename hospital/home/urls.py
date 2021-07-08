from django.urls import path
from . import views
from treatment import views as treatment_views

urlpatterns = [
    path('', views.showHome, name='index'),
    path('about-med-care', views.showAbout, name='about'),
    path('contact-us', views.showContact, name='contact'),
    path('receptionist-dashboard', views.showReceptionistBoard, name='receptionist_dashboard'),
    path('receptionist-dashboard/patients', treatment_views.showPatients, name='patients'),
    path('receptionist-dashboard/patients/update/<int:id>', treatment_views.updatePatient, name='patient_update'),
    path('receptionist-dashboard/appointments', views.showAppointments, name='appointments'),
    path('receptionist-dashboard/appointments/update/<int:id>', views.updateAppointment, name='appointment_update'),
    path('receptionist-dashboard/appointments/delete/<int:id>', views.deleteAppointment),
    path('receptionist-dashboard/create-appointment', views.createAppointment, name='appointment'),
    path('receptionist-dashboard/invoices', views.showInvoices, name='invoices'),
    path('receptionist-dashboard/invoices/<str:pk>/', views.showInvoice, name='show_invoice'),
    path('receptionist-dashboard/invoices/update/<int:id>', views.updateInvoice, name='invoice_update'),
    path('receptionist-dashboard/issue-invoice', views.issueInvoice, name='invoice'),
    path('admin-dashboard', views.showAdminBoard, name='admin_dashboard'),
    path('admin-dashboard/patients', treatment_views.showPatients, name='patients_adm'),
    path('admin-dashboard/invoices', views.showInvoices, name='invoices_adm'),
    path('admin-dashboard/invoices/<str:pk>/', views.showInvoice, name='show_invoice'),
    path('admin-dashboard/invoices/update/<int:id>', views.updateInvoiceAdm, name='invoice_update_adm'),
]
