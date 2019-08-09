from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django.contrib.auth.models import User


class CustomUserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        # model = CustomUser
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # fields = UserCreationForm.Meta.fields
    def save(self, commit=True):
        user = super(CustomUserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
