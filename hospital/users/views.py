import urllib.request
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileEditForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.decorators import login_required#, permission_required
from django.contrib import messages
from .models import CustomUser
from treatment.models import Patient
from django.core.mail import send_mail
from django.template.loader import render_to_string

def create(request):
    form = CustomUserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            messages.success(request, (name + ' has been added successfully'))
            return redirect('account')
        else:
            messages.error(request, "Please review and correct form input fields")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/account.html', {'form': form})

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
                'yustaoab@gmail.com',
                [email],
                fail_silently=False,
                html_message = render_to_string('users/change_password_email.html', {'name': str(name)})
            )
            messages.success(request, "Your password has been changed")
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})

@login_required
def editProfile(request, **kwargs):
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been modified")
            return redirect('edit_profile')
        else:
            messages.error(request, "Error: Please review form input fields below")
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})
