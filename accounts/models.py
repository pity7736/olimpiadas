from django.contrib.auth.models import AbstractUser
from accounts.managers import UserManager


class User(AbstractUser):

    objects = UserManager()
