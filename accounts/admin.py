from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomStudentChangeForm, CustomStudentFrom

# Register your models here.

UserModel = get_user_model()

@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    form = CustomStudentChangeForm
    add_form = CustomStudentFrom

    list_display = ('username', 'email')

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", 'faculty_number', "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        (None, {'fields': ('email', 'password', 'can_make_reports')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )