from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreateForm


class SignUpView(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'