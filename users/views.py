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

class VerificationEmailView(TemplateView):
    template_name = "users/verification_email_form.html"

    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            self.send_verification_email(request, user)
        except User.DoesNotExist:
            pass  # Обработайте ошибку, если пользователь с таким email не существует
        return redirect('users:email_verification_done')

    def send_verification_email(self, request, user):
        current_site = get_current_site(request)
        # Создаем токен для подтверждения адреса электронной почты
        token = default_token_generator.make_token(user)
        # Закодируем ID пользователя и токен для использования в URL
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = urlsafe_base64_encode(force_bytes(token))
        # Создаем URL для подтверждения адреса электронной почты
        verification_url = reverse('users:email_verification_confirm', kwargs={'uidb64': uid, 'token': token})
        # Создаем контекст для шаблона письма
        context = {
            'user': user,
            'verification_url': verification_url,
            'domain': current_site.domain,
        }
        # Отправляем письмо с подтверждением
        subject = 'Подтверждение адреса электронной почты'
        message = render_to_string('users/verification_email.html', context)
        send_mail(subject, message, 'noreply@oscarbot.ru', [user.email])


class VerificationEmailConfirmView(TemplateView):
    template_name = 'users/verification_email_confirm.html'

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.email_verified = True
                user.save()
                return super().get(request)
            else:
                return render(request, 'users/verification_email_invalid.html')
        except User.DoesNotExist:
            return render(request, 'users/verification_email_invalid.html')


class VerificationEmailCompleteView(TemplateView):
    template_name = 'users/verification_email_complete.html'


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy('users:login')


    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     user = form.save()
    #     self.send_verification_email(user)
    #     return response
    #
    # def send_verification_email(self, user):
    #     current_site = get_current_site(self.request)
    #     # Создаем токен для подтверждения адреса электронной почты
    #     token = default_token_generator.make_token(user)
    #     # Закодируем ID пользователя и токен для использования в URL
    #     uid = urlsafe_base64_encode(force_bytes(user.pk))
    #     token = urlsafe_base64_encode(force_bytes(token))
    #     # Создаем URL для подтверждения адреса электронной почты
    #     verification_url = reverse('users:email_verification_confirm', kwargs={'uidb64': uid, 'token': token})
    #     # Создаем контекст для шаблона письма
    #     context = {
    #         'user': user,
    #         'verification_url': verification_url,
    #         'domain': current_site.domain,
    #     }
    #     # Отправляем письмо с подтверждением
    #     subject = 'Подтверждение адреса электронной почты'
    #     message = render_to_string('users/verification_email.html', context)
    #     send_mail(subject, message, 'noreply@oscarbot.ru', [user.email])


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