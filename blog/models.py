from khayyam import *

# Create your models here.
from datetime import time
import time
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class WorkBox(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())
    title = JalaliDatetime.now().strftime('%C');



class Work(models.Model):

    title = models.CharField(max_length=30 , null=False , default="کار");
    beginnig_time = models.CharField(max_length=30 , default = str(time.strftime("%H:%M")))
    finish_time = models.CharField(default = None , null=True , max_length=30);
    workbox = models.ForeignKey(WorkBox, on_delete=models.CASCADE)
    isFinished = models.BooleanField(default= False)
    d = models.CharField(default = None , null=True , max_length=30);
    def __str__(self):
        return self.title;


class MyUserManager(BaseUserManager):
    def create_user(self, email,avatar = "blog/image/anynom.jpg" ,  name = "ناشناس", phone= "", password=None ):
        if not email:
            raise ValueError('وارد کردن ایمیل ضروری است!')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            name = name,
            phone = phone,
            avatar = avatar,
            password = password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,
                                password=password,

                                )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    name = models.CharField(max_length=50 , default="ناشناس")
    phone = models.CharField(max_length=50 , default="0")
    avatar = models.ImageField(default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # For this case we return email. Could also be User.first_name User.last_name if you have these fields
        return self.name

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin


