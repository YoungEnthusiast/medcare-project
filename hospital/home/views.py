from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, AppointmentForm, InvoiceForm
from .models import Contact, Appointment, Invoice, Receptionist
from django.contrib.auth.decorators import login_required, permission_required
from .filters import AppointmentFilter, InvoiceFilter
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from treatment.models import Doctor
import random
from django.urls import reverse_lazy
from datetime import date
#from django.views.generic import UpdateView
from django.core.mail import send_mail
from django.template.loader import render_to_string

def showHome(request):
    return render(request, 'home/home.html')

def showAbout(request):
    return render(request, 'home/about.html')

def handler400(request, exception):
    context = {}
    response = render(request, "home/400.html", context=context)
    response.status_code = 400
    return response

def handler403(request, exception):
    context = {}
    response = render(request, "home/403.html", context=context)
    response.status_code = 403
    return response

def handler404(request, exception):
    context = {}
    response = render(request, "home/404.html", context=context)
    response.status_code = 404
    return response

def handler500(request):
    context = {}
    response = render(request, "home/500.html", context=context)
    response.status_code = 500
    return response

def handler502(request, exception):
    context = {}
    response = render(request, "home/502.html", context=context)
    response.status_code = 502
    return response

def showContact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            send_mail(
                'Contact Med Care',
                'A message was sent by ' + name + '. Please log in to admin panel to read message',
                'yustaoab@gmail.com',
                [email],
                fail_silently=False,
                #html_message = render_to_string('home/home1.html')
            )
            messages.success(request, str(name) + ", your message will receive attention shortly")
        else:
            return redirect('contact')
    return render(request, 'home/contact_form.html', {'form': form})

@login_required
@permission_required('home.view_appointment')
@permission_required('home.view_receptionist')
@permission_required('treatment.view_doctor')
@permission_required('treatment.view_patient')
def showReceptionistBoard(request):
    appointments = Appointment.objects.all()
    done = Appointment.objects.filter(status = 1).count()
    pending = Appointment.objects.filter(status = 0).count()

    doctors = Doctor.objects.all()
    busy = Doctor.objects.filter(busy = 1).count()
    available = Doctor.objects.filter(busy = 0).count()
    try:
        doc1 = Doctor.objects.filter(busy=0)[0]
    except:
        doc1 = " "
    try:
        doc2 = Doctor.objects.filter(busy=0)[1]
    except:
        doc2 = " "
    try:
        doc3 = Doctor.objects.filter(busy=0)[2]
    except:
        doc3 = " "
    try:
        next = Appointment.objects.filter(status = 0).order_by('created')[0]
    except:
        next = ""
    try:
        second = Appointment.objects.filter(status = 0).order_by('created')[1]
    except:
        second = ""

    context = {'pending':pending, 'next':next, 'second': second,  'busy':busy, 'available':available, 'doc1':doc1, 'doc2':doc2, 'doc3':doc3}
    return render(request, 'home/receptionist_dashboard.html', context)

@login_required
@permission_required('home.view_appointment')
def showAppointmentsRec(request):
    context = {}
    filtered_appointments = AppointmentFilter(
        request.GET,
        queryset = Appointment.objects.all()
    )
    context['filtered_appointments'] = filtered_appointments
    paginated_filtered_appointments = Paginator(filtered_appointments.qs, 10)
    page_number = request.GET.get('page')
    appointments_page_obj = paginated_filtered_appointments.get_page(page_number)
    context['appointments_page_obj'] = appointments_page_obj
    total_appointments = filtered_appointments.qs.count()
    context['total_appointments'] = total_appointments
    return render(request, 'home/appointments_rec.html', context=context)

@login_required
@permission_required('home.view_appointment')
def showAppointmentsDoc(request):
    context = {}
    filtered_appointments = AppointmentFilter(
        request.GET,
        queryset = Appointment.objects.all()
    )
    context['filtered_appointments'] = filtered_appointments
    paginated_filtered_appointments = Paginator(filtered_appointments.qs, 10)
    page_number = request.GET.get('page')
    appointments_page_obj = paginated_filtered_appointments.get_page(page_number)
    context['appointments_page_obj'] = appointments_page_obj
    total_appointments = filtered_appointments.qs.count()
    context['total_appointments'] = total_appointments
    return render(request, 'home/appointments_doc.html', context=context)

@login_required
@permission_required('home.change_appointment')
def updateAppointment(request, id):
    appointment = Appointment.objects.get(id=id)
    form = AppointmentForm(instance=appointment)
    if request.method=='POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "The appointment has been modified successfully")
            return redirect('appointments')
    return render(request, 'home/appointment_form_update.html', {'form': form, 'appointment': appointment})

@login_required
@permission_required('home.change_appointment')
def updateAppointmentDoc(request, id):
    appointment = Appointment.objects.get(id=id)
    form = AppointmentForm(instance=appointment)
    if request.method=='POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "The appointment has been modified successfully")
            return redirect('appointments_doc')
    return render(request, 'home/appointment_form_update.html', {'form': form, 'appointment': appointment})

@login_required
@permission_required('home.view_appointment')
def deleteAppointment(request, id):
    appointment = Appointment.objects.get(id=id)
    obj = get_object_or_404(Appointment, id = id)
    if request.method =="POST":
        obj.delete()
        return redirect('appointments')
    context = {'appointment': appointment}
    return render(request, 'home/appointment_confirm_delete.html', context)

@login_required
@permission_required('home.view_appointment')
def deleteAppointmentDoc(request, id):
    appointment = Appointment.objects.get(id=id)
    obj = get_object_or_404(Appointment, id = id)
    if request.method =="POST":
        obj.delete()
        return redirect('appointments_doc')
    context = {'appointment': appointment}
    return render(request, 'home/appointment_confirm_delete.html', context)

@login_required
@permission_required('home.add_appointment')
def createAppointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            form.save()
            reg = Appointment.objects.filter(appointment_Id=2021)[0]
            reg.appointment_Id = "MCH" + str(random.randint(10000,99999))
            reg.receptionist = request.user.first_name
            reg.save()
            #patient = form.cleaned_data.get('patient')
            #doctor = form.cleaned_data.get('doctor')
            receptionist = reg.receptionist
            appointment_id = reg.appointment_Id
            first_name = reg.patient.user.first_name
            patient_id = reg.patient.user.username
            doc_email = reg.doctor.user.email
            send_mail(
                'NEW PATIENT APPOINTMENT',
                'You have been assigned to a new patient whose ID is: ' + str(patient_id) + '. The appointment ID is: ' + str(appointment_id) + '.',
                'yustaoab@gmail.com',
                [doc_email],
                fail_silently=False,
                html_message = render_to_string('treatment/doc_appointment_email.html', {'receptionist': str(receptionist), 'first_name': str(first_name), 'patient_id': str(patient_id), 'appointment_id': str(appointment_id)})
            )
            messages.success(request, str(first_name) + "'s appointment has been added successfully")
        else:
            return redirect('appointment')
    return render(request, 'home/appointment_form.html', {'form': form})

@login_required
@permission_required('home.view_invoice')
def showInvoices(request):
    context = {}
    filtered_invoices = InvoiceFilter(
        request.GET,
        queryset = Invoice.objects.all()
    )
    context['filtered_invoices'] = filtered_invoices
    paginated_filtered_invoices = Paginator(filtered_invoices.qs, 10)
    page_number = request.GET.get('page')
    invoices_page_obj = paginated_filtered_invoices.get_page(page_number)
    context['invoices_page_obj'] = invoices_page_obj
    total_invoices = filtered_invoices.qs.count()
    context['total_invoices'] = total_invoices
    return render(request, 'home/invoices.html', context=context)

@login_required
@permission_required('home.view_invoice')
def showInvoicesRec(request):
    context = {}
    filtered_invoices = InvoiceFilter(
        request.GET,
        queryset = Invoice.objects.all()
    )
    context['filtered_invoices'] = filtered_invoices
    paginated_filtered_invoices = Paginator(filtered_invoices.qs, 10)
    page_number = request.GET.get('page')
    invoices_page_obj = paginated_filtered_invoices.get_page(page_number)
    context['invoices_page_obj'] = invoices_page_obj
    total_invoices = filtered_invoices.qs.count()
    context['total_invoices'] = total_invoices
    return render(request, 'home/invoices_rec.html', context=context)

@login_required
def updateInvoiceAdm(request, id):
    invoice = Invoice.objects.get(id=id)
    form = InvoiceForm(instance=invoice)
    if request.method=='POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            receptionist = form.cleaned_data.get('receptionist')
            appointment = form.cleaned_data.get('appointment')
            admin = form.cleaned_data.get('admin')
            if admin == None:
                messages.error(request, "Please select an admin before submission")
            else:
                appointment_Id = appointment.appointment_Id
                patient_id = appointment.patient
                rec_name = receptionist.user.first_name
                rec_email = receptionist.user.email
                admin_name = admin.user.first_name
                send_mail(
                    'INVOICE CONFIRMED',
                    '',
                    'yustaoab@gmail.com',
                    [rec_email],
                    fail_silently=False,
                    html_message = render_to_string('home/invoice_confirmed_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'rec_name': str(rec_name), 'admin_name': str(admin_name)})
                )
                messages.success(request, "The invoice has been confirmed successfully")
                return redirect('invoices_adm')


    return render(request, 'home/invoice_form_update.html', {'form': form, 'invoice': invoice})

# class InvoiceUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
# #class InvoiceUpdateView(SuccessMessageMixin, UpdateView):
#     model = Invoice
#     template_name = 'home/invoice_form_update.html'
#     success_url = reverse_lazy('invoices_adm')
#     #success_message = "%(username)s was created"
#     success_message = "The invoice has been confirmed successfully"
#     fields = ('confirmation', 'admin')
#     permission_required = 'home.change_invoice'
#
#     def form_valid(self, form):
#         receptionist = form.cleaned_data.get('receptionist')
#         appointment = form.cleaned_data.get('appointment')
#         admin = form.cleaned_data.get('admin')
#         if admin == None:
#             pass
#         else:
#             appointment_Id = appointment.appointment_Id
#             patient_id = appointment.patient
#             rec_name = receptionist.user.first_name
#             rec_email = receptionist.user.email
#             admin_name = admin.user.first_name
#             send_mail(
#                 'INVOICE CONFIRMED',
#                 '',
#                 'yustaoab@gmail.com',
#                 [rec_email],
#                 fail_silently=False,
#                 html_message = render_to_string('home/invoice_confirmed_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'rec_name': str(rec_name), 'admin_name': str(admin_name)})
#             )
#             return super(InvoiceUpdateView, self).form_valid(form)

@login_required
@permission_required('home.add_invoice')
def issueInvoice(request):
    form = InvoiceForm()
    if request.method == 'POST':
        form = InvoiceForm(request.POST or None)
        if form.is_valid():
            form.save()
            reg = Invoice.objects.all()[0]
            receptionist = form.cleaned_data.get('receptionist')
            appointment = form.cleaned_data.get('appointment')
            admin = form.cleaned_data.get('admin')
            appointment_Id = appointment.appointment_Id
            patient_id = appointment.patient
            rec_name = receptionist.user.first_name
            total = reg.total()
            try:
                admin_email = admin.user.email
                admin_name = admin.user.first_name
            except:
                pass
            if reg.confirmation == False and reg.admin == None:
                messages.error(request, "Please tick the confirmation box or select an admin that will confirm")
                reg.delete()
            if reg.confirmation == False and reg.admin != None:
                send_mail(
                    'PLEASE CONFIRM INVOICE',
                    '',
                    'yustaoab@gmail.com',
                    [admin_email],
                    fail_silently=False,
                    html_message = render_to_string('home/request_confirm_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'rec_name': str(rec_name), 'admin_name': str(admin_name), 'total': str(total)})
                )
                messages.success(request, str(appointment.patient.user.first_name) + "'s invoice has been saved successfully")
                return redirect('invoices_rec')

            elif reg.confirmation == True and reg.admin == None:
                messages.success(request, str(appointment.patient.user.first_name) + "'s invoice has been saved successfully")
                return redirect('invoices_rec')
            elif reg.confirmation == True and reg.admin != None:
                messages.error(request, "You cannot tick the confirmation box and at the same time select an admin again")
                reg.delete()
        else:
            return redirect('invoice')
    return render(request, 'home/invoice_form.html', {'form': form})

@login_required
@permission_required('home.view_invoice')
def showInvoice(request, pk, **kwargs):
    invoice = Invoice.objects.get(id=pk)
    context = {'invoice': invoice}
    return render(request, 'home/invoice_detail.html', context)

@login_required
@permission_required('home.view_invoice')
@permission_required('home.view_hr')
@permission_required('home.change_invoice')
@permission_required('home.view_appointment')
@permission_required('treatment.view_patient')
def showAdminBoard(request):
    invoices = Invoice.objects.all()
    today_invoices = Invoice.objects.filter(created__contains=date.today())
    all_total = 0
    today_total = 0
    for each in invoices:
        if each.total() != None:
            all_total = all_total + each.total()
        else:
            all_total = all_total
    for each2 in today_invoices:
        if each2.total() != None:
            today_total = today_total + each2.total()
        else:
            today_total = today_total
    try:
        last_invoice = Invoice.objects.filter(created__contains=date.today())[0]
        last_amount = last_invoice.total()
    except:
        last_amount = " "
    try:
        next = Appointment.objects.filter(status = 0).order_by('created')[0]
    except:
        next = ""

    context = {'all_total':all_total, 'today_total':today_total, 'last_amount':last_amount, 'next':next}
    return render(request, 'home/admin_dashboard.html', context)
