from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    exclude = ('user_permissions', 'groups')
    readonly_fields = ('last_login',)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email', 'password', 'first_name', 'last_name',
                    'is_staff', 'is_active', 'date_joined', 'last_login',
                )
            },
        ),
    )

    ordering = ('email',)
    filter_horizontal = ()
