from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreateForm


class SignUpView(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)

    def form_invalid(self, form):
        return super(SignUpView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "base"

    def form_valid(self, form):
        self.user = form.get_user()

        # user authentication
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


@login_required
def logout_view(request):
    logout(request)
    return redirect('base')
