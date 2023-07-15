from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserUpdate
from users.models import User


# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy('users:login')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdate
    template_name = "users/update_user.html"
    success_url = reverse_lazy('catalog:index')

    def get_object(self, queryset=None):
        return self.request.user


