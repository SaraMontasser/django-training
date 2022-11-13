from django.contrib import admin
from django import forms
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
# Register your models here.

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
        widgets = {
            'bio': forms.Textarea,
        }

class UserAdmin( BaseUserAdmin ):
    form = UserForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


admin.site.register(User, UserAdmin)