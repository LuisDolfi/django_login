from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        remember = self.request.POST.get('remember_me')
        if remember:
            self.request.session.set_expiry(60 * 60 * 24 * 14)  # 14 días
            messages.success(self.request, 'Te recordamos por 14 días.')
        else:
            self.request.session.set_expiry(0)  # se cierra al cerrar el navegador
        return response

class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Cuenta creada. Iniciá sesión.')
        return super().form_valid(form)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
