import urllib.request
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomRegisterForm, UserEditForm, PersonEditForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.decorators import login_required#, permission_required
from .models import Person
from home.models import Receptionist, HR
from treatment.models import Patient, Doctor, LabScientist, Nurse, Pharmacist
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template.loader import render_to_string

# def create(request):
#     if request.method == "POST":
#         form = CustomRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('edit_profile0')
#
#             # name = form.cleaned_data.get('first_name')
#             # email = form.cleaned_data.get('email')
#             # messages.success(request,  ('Added successfully! Please complete registration by filling the form below'))
#             # return redirect('edit_profile')
#         else:
#             messages.error(request, "Please review and correct form input fields")
#             #return redirect('account')
#     else:
#         form = CustomRegisterForm()
#     return render(request, 'users/account.html', {'form': form})

@login_required
def editProfile0(request, **kwargs):
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=request.user)
        person_form = PersonEditForm(request.POST, instance=request.user.person)

        if form.is_valid() and person_form.is_valid():
            form.save()
            person_form.save()
            new_person = Person.objects.get(user=request.user)
            new_person.save()

            if new_person.role == "Patient":
                new_patient = Patient()
                new_patient.user = new_person.user
                new_patient.first_name = new_person.user.first_name
                new_patient.last_name = new_person.user.last_name
                new_patient.phone_number = new_person.phone_number
                new_patient.gender = new_person.gender
                new_patient.address = new_person.address
                new_patient.age = new_person.age
                new_patient.blood_group = new_person.blood_group
                new_patient.retainer = new_person.retainer
                new_patient.created = new_person.created
                #new_patient.modified = new_person.modified
                new_patient.save()
                messages.success(request, "The Profile has been modified successfully")
                return redirect('receptionist_dashboard')
            elif new_person.role == "Doctor":
                new_doctor = Doctor()
                new_doctor.user = new_person.user
                new_doctor.save()
                messages.success(request, "The Profile has been modified successfully")
                return redirect('doctor_dashboard')
            elif new_person.role == "Front Desk Officer":
                new_receptionist = Receptionist()
                new_receptionist.user = new_person.user
                new_receptionist.save()
                messages.success(request, "The Profile has been modified successfully")
                return redirect('receptionist_dashboard')
            elif new_person.role == "Lab Technician":
                new_lab_tech = LabScientist()
                new_lab_tech.user = new_person.user
                new_lab_tech.save()
                messages.success(request, "The Profile has been modified successfully")
                return redirect('lab_sc_dashboard')
            elif new_person.role == "Nurse":
                new_nurse = Nurse()
                new_nurse.user = new_person.user
                new_nurse.save()
                messages.success(request, "The Profile has been modified successfully")
                return redirect('nurse_dashboard')
            elif new_person.role == "Pharmacist":
                new_pharmacist = Pharmacist()
                new_pharmacist.user = new_person.user
                new_pharmacist.save()
                messages.success(request, "The Profile has been modified successfully")
                return redirect('pharmacist_dashboard')
            elif new_person.role == "Admin":
                new_admin = HR()
                new_admin.user = new_person.user
                new_admin.save()
                messages.success(request, "The Profile has been modified successfully")
                return redirect('admin_dashboard')

        else:
            messages.error(request, "Error: Please review form input fields below")
    else:
        form = UserEditForm(instance=request.user)
        person_form = PersonEditForm(instance=request.user.person)
    return render(request, 'users/edit_profile.html', {'form': form, 'person_form': person_form})

@login_required
def editProfile(request, **kwargs):
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=request.user)
        person_form = PersonEditForm(request.POST, instance=request.user.person)
        if form.is_valid() and person_form.is_valid():
            form.save()
            person_form.save()
            new_person = Person.objects.get(user=request.user)
            new_person.save()
            messages.success(request, "Your profile has been modified successfully")
            return redirect('edit_profile')
        else:
            messages.error(request, "Error: Please review form input fields below")
    else:
        form = UserEditForm(instance=request.user)
        person_form = PersonEditForm(instance=request.user.person)
    return render(request, 'users/edit_profile.html', {'form': form, 'person_form': person_form})


@login_required
def changePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            user = request.user
            name = user.first_name
            email = user.email
            send_mail(
                'Password Changed!',
                'Dear ' + str(name) + ', your password has just been changed. If this activity was not carried out by you, please reply to this email',
                'info@medcarehospitals.com.ng',
                [email],
                fail_silently=False,
                html_message = render_to_string('users/change_password_email.html', {'name': str(name)})
            )
            messages.success(request, "Your password has been changed")
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})

# @login_required
# def editProfile(request, **kwargs):
#     if request.method == "POST":
#         form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your profile has been modified")
#             return redirect('edit_profile')
#         else:
#             messages.error(request, "Error: Please review form input fields below")
#     else:
#         form = ProfileEditForm(instance=request.user)
#     return render(request, 'users/edit_profile.html', {'form': form})
