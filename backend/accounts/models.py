from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        default="",
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name="이메일",
    )

    age_choices = [
        (f"{str(age)}대", f"{str(age)}대")
        for age in range(10, 81, 10)
    ]
    age_choices.append(("선택", "선택"))

    age_range = models.CharField(
        max_length=50,
        choices=age_choices,
        default="선택",
        verbose_name="연령대"
        )
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="가입 일시")
    last_login = models.DateTimeField(auto_now=True, verbose_name="최종 로그인 일시")

    is_active = models.BooleanField(default=True, verbose_name="활성화 여부")
    is_admin = models.BooleanField(default=False, verbose_name="스태프 여부")

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    class Meta:
        verbose_name = "유저"
        verbose_name_plural = "유저"

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
