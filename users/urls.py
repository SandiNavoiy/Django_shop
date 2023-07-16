from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from catalog.views import UserPasswordResetView
from users.apps import UsersConfig

from users.views import RegisterView, UserUpdateView, CustomPasswordResetView, CustomPasswordResetDoneView, \
    CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('reset_password/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('email_verification/', VerificationEmailConfirmView.as_view(), name='email_verification_confirm'),
    # path('email_verification/complete/', VerificationEmailCompleteView.as_view(), name='email_verification_complete'),

]
