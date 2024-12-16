from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, email, password, agreed_to_terms_and_p_policy=False, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_('User must have an email address'))
        if not username:
            raise ValueError(_('User must have a username'))
        if not agreed_to_terms_and_p_policy:
            raise ValueError("Users must agree to the terms and privacy policy.")
        user = self.model(username=username,
                          email=self.normalize_email(email),
                          agreed_to_terms_and_p_policy=agreed_to_terms_and_p_policy,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(username, email, password, **extra_fields)