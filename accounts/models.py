from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _

# from .managers import UserManager


class User(AbstractBaseUser):
    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'mentor'),
    ) 

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField('username', max_length=200, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('active'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def save(self, *args, **kwargs):
       self.username = self.email
       super(User, self).save(*args, **kwargs)

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.email
        return full_name

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name