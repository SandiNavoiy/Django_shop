from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email = 'admin1@admin.ru',
            first_name = 'Admin',
            last_name = 'Admin',
            is_staff = True,
            is_superuser = True
        )
        user.set_password('kaliningrad39')  #установка пароля
        user.save()  # сохраниние в БД
