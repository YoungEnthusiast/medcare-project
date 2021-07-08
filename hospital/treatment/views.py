from django.shortcuts import render, redirect
from home.models import Appointment
from django.contrib.auth.decorators import login_required, permission_required
from .filters import ConsultationFilter
from users.filters import PatientFilter
from django.core.paginator import Paginator
from django.contrib import messages
from users.models import Person
from .models import Doctor, Consultation, Patient
from .forms import DoctorForm, ConsultationForm, PatientForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
#from users.models import AdaptedUser
#from users.forms import PersonEditForm

@login_required
def showPatients(request):
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
    return render(request, 'treatment/patients.html', context=context)

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
        return render(request, 'treatment/consultations0.html')


@login_required
@permission_required('treatment.add_consultation')
def createConsultation(request):
    form = ConsultationForm()
    if request.method == 'POST':
        form = ConsultationForm(request.POST or None)
        if form.is_valid():
            form.save()
            patient = form.cleaned_data.get('patient')
            email = form.cleaned_data.get('email')
            messages.success(request, str(patient) + "'s appointment has been added successfully")
        else:
            return redirect('new_history')
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
def updateConsultation(request, id):
    consultation = Consultation.objects.get(id=id)
    form = ConsultationForm(instance=consultation)
    if request.method=='POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            messages.success(request, "The medical history has been modified successfully")
            return redirect('consultations')
    return render(request, 'treatment/consultation_form_update.html', {'form': form, 'consultation': consultation})

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
            messages.success(request, "The medical history has been modified successfully")
            return redirect('consultations_lab')
    return render(request, 'treatment/consultation_form_update.html', {'form': form, 'consultation': consultation})
