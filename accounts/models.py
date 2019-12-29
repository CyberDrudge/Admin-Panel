from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, user_id, password, is_staff=False, is_admin=False):
        if not user_id:
            raise ValueError("User must have an user id.")
        if not password:
            raise ValueError("User must have a password.")

        user_obj = self.model(
            user_id=user_id,
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, user_id, password):
        user = self.create_user(user_id, password, is_staff=True)
        return user

    def create_superuser(self, user_id, password):
        user = self.create_user(user_id, password, is_staff=True, is_admin=True)
        return user


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=120, unique=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.user_id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
