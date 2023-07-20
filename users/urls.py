from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import RegisterView, UserUpdateView, ActivationFailed, \
    ActivationOk, activate_account, gen_pass, UserForgotPasswordView, UserPasswordResetConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('', never_cache(LoginView.as_view(template_name='users/login.html')), name='login'),
    path('logout/', never_cache(LogoutView.as_view(), name='logout')),
    path('register/', never_cache(RegisterView.as_view()), name='register'),
    path('update/', never_cache(UserUpdateView.as_view()), name='update'),
    path('register/', never_cache(RegisterView.as_view()), name='register'),
    path('verify/<str:uidb64>/', activate_account, name='email_verification'),
    path('success', never_cache(ActivationOk.as_view()), name='activation_ok'),
    path('failed', never_cache(ActivationFailed.as_view()), name='activation_failed'),
    path("gen_pass/", gen_pass, name="gen_pass"),
    path('password-reset/', never_cache(UserForgotPasswordView.as_view()), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', never_cache(UserPasswordResetConfirmView.as_view()), name='password_reset_confirm'),

]
