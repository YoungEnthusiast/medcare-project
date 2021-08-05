from django.shortcuts import render, redirect
from home.models import Appointment
from inventory.models import Injection, Tablet, Syrup, Suppository
from inventory.forms import InjectionForm, TabletForm, SyrupForm, SuppositoryForm
from django.contrib.auth.decorators import login_required, permission_required
from .filters import ConsultationFilter
from users.filters import PatientFilter
from inventory.filters import InjectionFilter, TabletFilter, SyrupFilter, SuppositoryFilter
from django.core.paginator import Paginator
from django.contrib import messages
from users.models import Person
from .models import Doctor, Consultation, Patient
from .forms import DoctorForm, ConsultationForm, ConsultationFormDoc, PatientForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
#from users.models import AdaptedUser
#from users.forms import PersonEditForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

@login_required
def showPatientsRec(request):
    context = {}
    filtered_patients = PatientFilter(
        request.GET,
        queryset = Patient.objects.all()
    )
    context['filtered_patients'] = filtered_patients
    paginated_filtered_patients = Paginator(filtered_patients.qs, 10)
    page_number = request.GET.get('page')
    patients_page_obj = paginated_filtered_patients.get_page(page_number)
    context['patients_page_obj'] = patients_page_obj
    total_patients = filtered_patients.qs.count()
    context['total_patients'] = total_patients
    return render(request, 'treatment/patients_rec.html', context=context)

@login_required
def showPatientsDoc(request):
    context = {}
    filtered_patients = PatientFilter(
        request.GET,
        queryset = Patient.objects.all()
    )
    context['filtered_patients'] = filtered_patients
    paginated_filtered_patients = Paginator(filtered_patients.qs, 10)
    page_number = request.GET.get('page')
    patients_page_obj = paginated_filtered_patients.get_page(page_number)
    context['patients_page_obj'] = patients_page_obj
    total_patients = filtered_patients.qs.count()
    context['total_patients'] = total_patients
    return render(request, 'treatment/patients_doc.html', context=context)

@login_required
def showPatientsLab(request):
    context = {}
    filtered_patients = PatientFilter(
        request.GET,
        queryset = Patient.objects.all()
    )
    context['filtered_patients'] = filtered_patients
    paginated_filtered_patients = Paginator(filtered_patients.qs, 10)
    page_number = request.GET.get('page')
    patients_page_obj = paginated_filtered_patients.get_page(page_number)
    context['patients_page_obj'] = patients_page_obj
    total_patients = filtered_patients.qs.count()
    context['total_patients'] = total_patients
    return render(request, 'treatment/patients_lab.html', context=context)

@login_required
def showPatientsNur(request):
    context = {}
    filtered_patients = PatientFilter(
        request.GET,
        queryset = Patient.objects.all()
    )
    context['filtered_patients'] = filtered_patients
    paginated_filtered_patients = Paginator(filtered_patients.qs, 10)
    page_number = request.GET.get('page')
    patients_page_obj = paginated_filtered_patients.get_page(page_number)
    context['patients_page_obj'] = patients_page_obj
    total_patients = filtered_patients.qs.count()
    context['total_patients'] = total_patients
    return render(request, 'treatment/patients_nur.html', context=context)

@login_required
def showPatientsPha(request):
    context = {}
    filtered_patients = PatientFilter(
        request.GET,
        queryset = Patient.objects.all()
    )
    context['filtered_patients'] = filtered_patients
    paginated_filtered_patients = Paginator(filtered_patients.qs, 10)
    page_number = request.GET.get('page')
    patients_page_obj = paginated_filtered_patients.get_page(page_number)
    context['patients_page_obj'] = patients_page_obj
    total_patients = filtered_patients.qs.count()
    context['total_patients'] = total_patients
    return render(request, 'treatment/patients_pha.html', context=context)

@login_required
def showPatientsAdm(request):
    context = {}
    filtered_patients = PatientFilter(
        request.GET,
        queryset = Patient.objects.all()
    )
    context['filtered_patients'] = filtered_patients
    paginated_filtered_patients = Paginator(filtered_patients.qs, 10)
    page_number = request.GET.get('page')
    patients_page_obj = paginated_filtered_patients.get_page(page_number)
    context['patients_page_obj'] = patients_page_obj
    total_patients = filtered_patients.qs.count()
    context['total_patients'] = total_patients
    return render(request, 'treatment/patients_adm.html', context=context)

@login_required
@permission_required('home.change_patient')
def updatePatient(request, id):
    patient = Person.objects.get(id=id)
    form = PatientForm(instance=patient)
    if request.method=='POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "The patient has been modified successfully")
            return redirect('patients')
    return render(request, 'treatment/patient_form_update.html', {'form': form, 'patient': patient})

@login_required
def showPatient(request, pk, **kwargs):
    patient = Patient.objects.get(id=pk)
    context = {'patient': patient}
    return render(request, 'treatment/patient_detail.html', context)

@login_required
@permission_required('treatment.view_doctor')
@permission_required('home.view_appointment')
@permission_required('treatment.view_patient')
@permission_required('treatment.view_consultation')
def showDoctorBoard(request):
    past = Appointment.objects.filter(status = 1, doctor__user=request.user).count()
    new = Appointment.objects.filter(status = 0, doctor__user=request.user).count()

    try:
        next = Appointment.objects.filter(status = 0).order_by('created')[0]
    except:
        next = ""

    try:
        last_date = Appointment.objects.filter(status=1, patient=next.patient).order_by('-created')[0]
    except:
        last_date = " "

    context = {'past':past, 'new':new, 'next':next, 'last_date':last_date}
    return render(request, 'treatment/doctor_dashboard.html', context)


@login_required
@permission_required('treatment.view_doctor')
def showDoctorStatus(request):
    doctor = Doctor.objects.get(user=request.user)
    context = {'doctor':doctor}
    return render(request, 'treatment/doctor_status.html', context)

@login_required
@permission_required('treatment.change_doctor')
def updateDoctorStatus(request, id):
    doctor = Doctor.objects.get(id=id)
    form = DoctorForm(instance=doctor)
    if request.method=='POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, "Your status has been modified successfully")
            return redirect('doctor_dashboard')
    return render(request, 'treatment/doctor_status_update.html', {'form': form, 'doctor': doctor})

@login_required
@permission_required('treatment.view_consultation')
def showConsultations(request):
    consultations = Consultation.objects.all().count()
    if consultations > 0:
        context = {}
        filtered_consultations = ConsultationFilter(
            request.GET,
            queryset = Consultation.objects.all()
        )
        context['filtered_consultations'] = filtered_consultations
        paginated_filtered_consultations = Paginator(filtered_consultations.qs, 10)
        page_number = request.GET.get('page')
        consultations_page_obj = paginated_filtered_consultations.get_page(page_number)
        context['consultations_page_obj'] = consultations_page_obj
        total_consultations = filtered_consultations.qs.count()
        context['total_consultations'] = total_consultations
        return render(request, 'treatment/consultations.html', context=context)
    else:
        return render(request, 'treatment/consultation0.html')

@login_required
@permission_required('treatment.view_consultation')
def showConsultationsDoc(request):
    consultations = Consultation.objects.all().count()
    if consultations > 0:
        context = {}
        filtered_consultations = ConsultationFilter(
            request.GET,
            queryset = Consultation.objects.all()
        )
        context['filtered_consultations'] = filtered_consultations
        paginated_filtered_consultations = Paginator(filtered_consultations.qs, 5)
        page_number = request.GET.get('page')
        consultations_page_obj = paginated_filtered_consultations.get_page(page_number)
        context['consultations_page_obj'] = consultations_page_obj
        total_consultations = filtered_consultations.qs.count()
        context['total_consultations'] = total_consultations
        return render(request, 'treatment/consultations_doc.html', context=context)
    else:
        return render(request, 'treatment/consultations_doc0.html')

@login_required
@permission_required('treatment.view_consultation')
def showConsultationsLab(request):
    consultations = Consultation.objects.all().count()
    if consultations > 0:
        context = {}
        filtered_consultations = ConsultationFilter(
            request.GET,
            queryset = Consultation.objects.all()
        )
        context['filtered_consultations'] = filtered_consultations
        paginated_filtered_consultations = Paginator(filtered_consultations.qs, 10)
        page_number = request.GET.get('page')
        consultations_page_obj = paginated_filtered_consultations.get_page(page_number)
        context['consultations_page_obj'] = consultations_page_obj
        total_consultations = filtered_consultations.qs.count()
        context['total_consultations'] = total_consultations
        return render(request, 'treatment/consultations_lab.html', context=context)
    else:
        return render(request, 'treatment/consultations_lab0.html')

@login_required
@permission_required('treatment.view_consultation')
def showConsultationsNur(request):
    consultations = Consultation.objects.all().count()
    if consultations > 0:
        context = {}
        filtered_consultations = ConsultationFilter(
            request.GET,
            queryset = Consultation.objects.all()
        )
        context['filtered_consultations'] = filtered_consultations
        paginated_filtered_consultations = Paginator(filtered_consultations.qs, 10)
        page_number = request.GET.get('page')
        consultations_page_obj = paginated_filtered_consultations.get_page(page_number)
        context['consultations_page_obj'] = consultations_page_obj
        total_consultations = filtered_consultations.qs.count()
        context['total_consultations'] = total_consultations
        return render(request, 'treatment/consultations_nur.html', context=context)
    else:
        return render(request, 'treatment/consultations_nur0.html')

@login_required
@permission_required('treatment.view_consultation')
def showConsultationsPha(request):
    consultations = Consultation.objects.all().count()
    if consultations > 0:
        context = {}
        filtered_consultations = ConsultationFilter(
            request.GET,
            queryset = Consultation.objects.all()
        )
        context['filtered_consultations'] = filtered_consultations
        paginated_filtered_consultations = Paginator(filtered_consultations.qs, 10)
        page_number = request.GET.get('page')
        consultations_page_obj = paginated_filtered_consultations.get_page(page_number)
        context['consultations_page_obj'] = consultations_page_obj
        total_consultations = filtered_consultations.qs.count()
        context['total_consultations'] = total_consultations
        return render(request, 'treatment/consultations_pha.html', context=context)
    else:
        return render(request, 'treatment/consultations_pha.html')

@login_required
@permission_required('treatment.add_consultation')
def createConsultation(request):
    form = ConsultationForm()
    if request.method == 'POST':
        form = ConsultationForm(request.POST or None)
        if form.is_valid():
            form.save()
            doctor = request.user
            doctor_name = doctor.last_name
            appointment = form.cleaned_data.get('appointment')
            lab_technician = form.cleaned_data.get('lab_technician')
            lab_technician_name = lab_technician.user.first_name
            lab_technician_email = lab_technician.user.email
            appointment_Id = appointment.appointment_Id
            patient_id = appointment.patient
            patient = appointment.patient.first_name
            send_mail(
                'NEW MESSAGE FROM DOCTOR',
                '',
                'info@medcarehospitals.com.ng',
                [lab_technician_email],
                fail_silently=False,
                html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            )
            messages.success(request, str(patient) + "'s appointment has been added successfully")
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'treatment/consultation_form.html', {'form': form})

@login_required
@permission_required('treatment.view_labscientist')
@permission_required('treatment.view_patient')
@permission_required('home.view_appointment')
def showLabScBoard(request):
    try:
        next = Appointment.objects.filter(status = 0).order_by('created')[0]
    except:
        next = ""
    context = {'next':next}
    return render(request, 'treatment/lab_sc_dashboard.html', context)

@login_required
@permission_required('treatment.view_nurse')
@permission_required('treatment.view_patient')
@permission_required('home.view_appointment')
def showNurseBoard(request):
    try:
        next = Appointment.objects.filter(status = 0).order_by('created')[0]
    except:
        next = ""
    context = {'next':next}
    return render(request, 'treatment/nurse_dashboard.html', context)


@login_required
@permission_required('treatment.view_pharmacist')
@permission_required('treatment.view_patient')
@permission_required('home.view_appointment')
def showPharmacistBoard(request):
    try:
        next = Appointment.objects.filter(status = 0).order_by('created')[0]
    except:
        next = ""
    context = {'next':next}
    return render(request, 'treatment/pharmacist_dashboard.html', context)

# class ConsultationUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
# #class InvoiceUpdateView(SuccessMessageMixin, UpdateView):
#     model = Consultation
#     template_name = 'treatment/consultation_form_update.html'
#     success_url = reverse_lazy('consultations')
#     #success_message = "%(username)s was created"
#     success_message = "The medical history has been modified successfully"
#     fields = ('test_result', 'prescription')
#     permission_required = 'treatment.change_consultation'

@login_required
@permission_required('treatment.change_consultation')
@permission_required('treatment.view_consultation')
def updateConsultationDoc(request, id):
    consultation = Consultation.objects.get(id=id)
    form = ConsultationFormDoc(instance=consultation)
    if request.method=='POST':
        form = ConsultationFormDoc(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            appointment = form.cleaned_data.get('appointment')
            #injection = form.cleaned_data.get('injection')
            injection_how = form.cleaned_data.get('injection_how')
            reg = Consultation.objects.filter(appointment=appointment)[0]

            reg.total = reg.myInjection + reg.myTablet + reg.mySyrup + reg.mySuppository

            # if reg.injection.price == None:
            #     reg.total = reg.tablet.price
            # elif reg.tablet.price == None:
            #     reg.total = reg.injection.price

            # if reg.injection == None:
            #     reg.total = reg.tablet.price + reg.syrup.price + reg.suppository.price







            reg.save()

            messages.success(request, "The medical history has been modified successfully")
            return redirect('consultations_doc')
    return render(request, 'treatment/consultation_form_update_doc.html', {'form': form, 'consultation': consultation})

@login_required
@permission_required('treatment.change_consultation')
@permission_required('treatment.view_consultation')
def updateConsultationLab(request, id):
    consultation = Consultation.objects.get(id=id)
    form = ConsultationForm(instance=consultation)
    if request.method=='POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            lab_technician = request.user
            lab_technician_name = lab_technician.first_name
            appointment = form.cleaned_data.get('appointment')
            appointment_Id = appointment.appointment_Id
            patient_id = appointment.patient
            patient = appointment.patient.first_name
            doctor_name = appointment.doctor
            doctor_email = appointment.doctor.user.email
            send_mail(
                'TEST RESULT FROM LABORATORY',
                '',
                'info@medcarehospitals.com.ng',
                [doctor_email],
                fail_silently=False,
                html_message = render_to_string('treatment/lab_doc_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name)})
            )
            messages.success(request, "The medical history has been modified successfully")
            return redirect('consultations_lab')
    return render(request, 'treatment/consultation_form_update_lab.html', {'form': form, 'consultation': consultation})

@login_required
def showInjections(request):
    context = {}
    filtered_injections = InjectionFilter(
        request.GET,
        queryset = Injection.objects.all()
    )
    context['filtered_injections'] = filtered_injections
    paginated_filtered_injections = Paginator(filtered_injections.qs, 10)
    page_number = request.GET.get('page')
    injections_page_obj = paginated_filtered_injections.get_page(page_number)
    context['injections_page_obj'] = injections_page_obj
    total_injections = filtered_injections.qs.count()
    context['total_injections'] = total_injections
    return render(request, 'inventory/injections.html', context=context)

@login_required
def updateInjection(request, id):
    injection = Injection.objects.get(id=id)
    form = InjectionForm(instance=injection)
    if request.method=='POST':
        form = InjectionForm(request.POST, instance=injection)
        if form.is_valid():
            form.save()
            messages.success(request, "The injection has been modified successfully")
            return redirect('injections')
    return render(request, 'inventory/injection_form_update.html', {'form': form, 'injection': injection})

@login_required
def addInjection(request):
    form = InjectionForm()
    if request.method == 'POST':
        form = InjectionForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, str(name) + " has been added successfully")
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'inventory/injection_form.html', {'form': form})

@login_required
def showTablets(request):
    context = {}
    filtered_tablets = TabletFilter(
        request.GET,
        queryset = Tablet.objects.all()
    )
    context['filtered_tablets'] = filtered_tablets
    paginated_filtered_tablets = Paginator(filtered_tablets.qs, 10)
    page_number = request.GET.get('page')
    tablets_page_obj = paginated_filtered_tablets.get_page(page_number)
    context['tablets_page_obj'] = tablets_page_obj
    total_tablets = filtered_tablets.qs.count()
    context['total_tablets'] = total_tablets
    return render(request, 'inventory/tablets.html', context=context)

@login_required
def updateTablet(request, id):
    tablet = Tablet.objects.get(id=id)
    form = TabletForm(instance=tablet)
    if request.method=='POST':
        form = TabletForm(request.POST, instance=tablet)
        if form.is_valid():
            form.save()
            messages.success(request, "The tablet has been modified successfully")
            return redirect('tablets')
    return render(request, 'inventory/tablet_form_update.html', {'form': form, 'tablet': tablet})

@login_required
def addTablet(request):
    form = TabletForm()
    if request.method == 'POST':
        form = TabletForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, str(name) + " has been added successfully")
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'inventory/tablet_form.html', {'form': form})

@login_required
def showSyrups(request):
    context = {}
    filtered_syrups = SyrupFilter(
        request.GET,
        queryset = Syrup.objects.all()
    )
    context['filtered_syrups'] = filtered_syrups
    paginated_filtered_syrups = Paginator(filtered_syrups.qs, 10)
    page_number = request.GET.get('page')
    syrups_page_obj = paginated_filtered_syrups.get_page(page_number)
    context['syrups_page_obj'] = syrups_page_obj
    total_syrups = filtered_syrups.qs.count()
    context['total_syrups'] = total_syrups
    return render(request, 'inventory/syrups.html', context=context)

@login_required
def updateSyrup(request, id):
    syrup = Syrup.objects.get(id=id)
    form = SyrupForm(instance=syrup)
    if request.method=='POST':
        form = SyrupForm(request.POST, instance=syrup)
        if form.is_valid():
            form.save()
            messages.success(request, "The syrup has been modified successfully")
            return redirect('syrups')
    return render(request, 'inventory/syrup_form_update.html', {'form': form, 'syrup': syrup})

@login_required
def addSyrup(request):
    form = SyrupForm()
    if request.method == 'POST':
        form = SyrupForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, str(name) + " has been added successfully")
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'inventory/syrup_form.html', {'form': form})

@login_required
def showSuppositories(request):
    context = {}
    filtered_suppositories = SuppositoryFilter(
        request.GET,
        queryset = Suppository.objects.all()
    )
    context['filtered_suppositories'] = filtered_suppositories
    paginated_filtered_suppositories = Paginator(filtered_suppositories.qs, 10)
    page_number = request.GET.get('page')
    suppositories_page_obj = paginated_filtered_suppositories.get_page(page_number)
    context['suppositories_page_obj'] = suppositories_page_obj
    total_suppositories = filtered_suppositories.qs.count()
    context['total_suppositories'] = total_suppositories
    return render(request, 'inventory/suppositories.html', context=context)

@login_required
def updateSuppository(request, id):
    suppository = Suppository.objects.get(id=id)
    form = SuppositoryForm(instance=suppository)
    if request.method=='POST':
        form = SuppositoryForm(request.POST, instance=suppository)
        if form.is_valid():
            form.save()
            messages.success(request, "The suppository has been modified successfully")
            return redirect('suppositories')
    return render(request, 'inventory/suppository_form_update.html', {'form': form, 'suppository': suppository})

@login_required
def addSuppository(request):
    form = SuppositoryForm()
    if request.method == 'POST':
        form = SuppositoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, str(name) + " has been added successfully")
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'inventory/suppository_form.html', {'form': form})
