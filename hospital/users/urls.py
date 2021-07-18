from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path('register', views.create, name='account'),
path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
path('complete-registration', views.editProfile0, name='edit_profile0'),
path('edit-profile', views.editProfile, name='edit_profile'),
path('change-password', views.changePassword, name='change_password'),
path('reset-password', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html'), name='reset_password'),
path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'), name='password_reset_done'),
path('reset-password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'), name='password_reset_confirm'),
path('reset-password-complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'), name='password_reset_complete'),
]
