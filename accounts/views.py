from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.utils.http import is_safe_url
from django.views.generic import CreateView, FormView, ListView
from django.contrib.auth import get_user_model
from .forms import LoginForm, RegisterForm
from admin_panel.mixins import RequestFormAttachMixin
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


# Create your views here.
class LoginView(RequestFormAttachMixin, FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = '/'
    default_next = '/'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(request, user_id=user_id, password=password)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("accounts:profile")
        return redirect("accounts:register")


class RegisterView(RequestFormAttachMixin, CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/'


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'accounts/profile.html'

    def get_queryset(self):
        return User.objects.all()


def delete_user(request):
    if request.method == "POST":
        pk = request.POST.get('delete_option', None)
        qs = User.objects.filter(id=pk)
        if qs.exists():
            qs.delete()
    return redirect("accounts:profile")
