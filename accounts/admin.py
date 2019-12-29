from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from .forms import UserAdminChangeForm, UserAdminCreationForm


User = get_user_model()


# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ('user_id', 'admin')
    list_filter = ('admin', 'staff',)
    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        ('Permissions', {'fields': ('admin', 'staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'password1', 'password2')}
        ),
    )
    search_fields = ('user_id',)
    ordering = ('user_id',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

