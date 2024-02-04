from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    model = CustomUser

    list_display = ["email", "age_range", "is_active", "is_staff", "date_joined"]

    list_display_links = ["email"]

    list_filter = ["email"]

    readonly_fields = ["last_login"]

    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (_("Permissions and Groups"), {"fields": ("is_active", "is_admin", "is_superuser",
                                                  "groups", "user_permissions")}),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2",),
        })
    )

    search_fields = ["email"]

admin.site.register(CustomUser, UserAdmin)
