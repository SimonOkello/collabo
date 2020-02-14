from django.contrib import admin
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

from jasim.models import MyUser


class UserAdmin(BaseUserAdmin):
    #  The forms to add and change user instances
    form = UserAdminCreationForm
    add_form = UserAdminChangeForm

    #  The fields to be used in displaying the User model
    #  These override the definitions on the base UserAdmin
    #  that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)})
    )
    #  add_fields is not a standard ModelAdmin attribute. UserAdmin
    #  overrides get_fieldsets to use this attribute when creating a user

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Register your models here.
admin.site.register(MyUser, UserAdmin)
# admin.site.register(Project)
# admin.site.register(Profile)
# admin.site.register(Review)


#  Remove Group Model from admin. We are not using it.
admin.site.unregister(Group)
