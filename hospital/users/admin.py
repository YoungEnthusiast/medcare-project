from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ['created', 'identifier', 'first_name', 'last_name', 'gender', 'is_staff']
    search_fields = ['identifier', 'email', 'phone_number']
    readonly_fields = ['username']
    list_filter = ['is_staff', 'is_superuser', 'retainer']
    list_editable = ['gender', 'is_staff']
    list_per_page = 10

    add_form = CustomUserCreationForm
    fieldsets = (
            *UserAdmin.fieldsets,
            (
                '',
                {
                    'fields': ('identifier', 'blood_group', 'retainer', 'phone_number', 'gender', 'address', 'age',)
                }
            )
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('identifier', 'email', 'first_name', 'last_name', 'phone_number', 'gender', 'address', 'age', 'blood_group', 'retainer', 'password1', 'password2')}
        ),
    )
admin.site.register(CustomUser, CustomUserAdmin)
