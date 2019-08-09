from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreateForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'surname', 'email',  'created_date']


admin.site.register(CustomUser, CustomUserAdmin)
