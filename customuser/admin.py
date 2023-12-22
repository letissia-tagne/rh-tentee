from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterCreationForm, RegisterChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = RegisterCreationForm
    form = RegisterChangeForm
    model = CustomUser
    list_display = ("username", "is_staff", "is_active",)
    list_filter = ("username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "position", "date_of_hire", "salary", "address"
, "phone_number", "department")}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)

admin.site.register(CustomUser, CustomUserAdmin)
