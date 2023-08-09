from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.base.Models.UserModels import UserModel
from api.base.forms import userModelCreationForm, userModelChangeForm


class userModelAdmin(UserAdmin):
    add_form = userModelCreationForm
    form = userModelChangeForm
    model = UserModel
    list_display = ('email', 'phone', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'last_login')
    list_filter = ('email', 'phone', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'last_login')
    fieldsets = (
        (None, {'fields': ('email', 'phone', 'password', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email', 'phone',)
    ordering = ('email', 'phone',)


admin.site.register(UserModel, userModelAdmin)
