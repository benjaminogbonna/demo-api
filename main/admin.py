from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', "email", 'name', 'date_joined', "is_staff", "is_active",)
    list_filter = ("is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ('username', "email", "password", 'name')}),
        ("Permissions", {"fields": (
            "is_active", "is_staff", 'is_superuser', 'address', 'city', 'country',
            "groups", "user_permissions", 'agreed_to_terms_and_p_policy', 'updated', 'date_joined', 'last_login')}
         ),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                'username', "email", "password1", "password2", 'agreed_to_terms_and_p_policy', "is_active",
                "groups", "user_permissions",
            )}),
    )
    search_fields = ('username', 'email', 'address', 'city', 'country')
    ordering = ("-date_joined",)
    readonly_fields = ('last_login', 'date_joined', 'updated')


admin.site.register(CustomUser, CustomUserAdmin)
