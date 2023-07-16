from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, UpdateView, TemplateView
from django.utils.encoding import force_str
from users.forms import UserRegisterForm, UserUpdate
from users.models import User


# Create your views here.

#

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy('users:login')
    def form_valid(self, form):
        # Генерируем уникальный токен для верификации
        user = form.save(commit=False)
        user.is_active = False  # Деактивируем пользователя, пока он не подтвердит почту
        user.set_unusable_password()  # Устанавливаем ненужный пароль
        user.save()

        # Отправляем письмо с токеном для верификации
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        current_site = get_current_site(self.request)
        mail_subject = 'Активация аккаунта'
        message = render_to_string(
            'users/verification_email.html',
            {
                'user': user,
                'domain': current_site.domain,
                'uid': uid,
                'token': token,
            }
        )
        send_mail(mail_subject, message, 'noreply@example.com', [user.email])
        return redirect('users:login')

class EmailVerificationView(PasswordResetConfirmView):
    template_name = "users/verification_confirm.html"
    success_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        # Получаем информацию о пользователе из URL-параметров
        uidb64 = kwargs['uidb64']
        token = kwargs['token']

        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            user = None

        # Проверяем, верен ли токен и активируем пользователя, если все в порядке
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.is_verified = True
            user.save()
            messages.success(request, 'Ваш аккаунт успешно активирован!')
            return self.get_redirect_url()
        else:
            messages.error(request, 'Неправильная ссылка активации аккаунта!')
            return self.get_redirect_url()




class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdate
    template_name = "users/update_user.html"
    success_url = reverse_lazy('catalog:index')

    def get_object(self, queryset=None):
        return self.request.user


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('users:password_reset_complete')
    template_name = 'users/password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'