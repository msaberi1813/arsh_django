from khayyam import *
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class WorkBox(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now())
    title = models.CharField(max_length=30 , default = str(JalaliDatetime.now().strftime('%H:%M:%S')))


class Work(models.Model):

    title = models.CharField(max_length=30 , null=False , default="کار");
    beginnig_time = models.TimeField(max_length=30 , default = JalaliDatetime.now().strftime('%G'))
    finish_time = models.TimeField(default = None , null=True , max_length=30);
    workbox = models.ForeignKey(WorkBox, on_delete=models.CASCADE)
    isFinished = models.BooleanField(default= False)

    @property
    def dd(self ):
        if (self.finish_time is None):
            return
        ss=str(self.beginnig_time)
        ff=str(self.finish_time)
        arr1 = ss.split(':')
        print(arr1[2])
        arr2 = ff.split(':')
        for i in range(len(arr1)):
            arr1[i] = str(arr1[i])
        for i in range(len(arr2)):
            arr1[i] = str(arr1[i])
        one = int(arr1[0]) * 3600 + int(arr1[1]) * 60 + int(arr1[2])
        if len(arr2) == 3:
            two = int(arr2[0]) * 3600 + int(arr2[1]) * 60 + int(arr2[2])
        else:
            two = int(arr2[0]) * 3600 + int(arr2[1]) * 60
        diff = two - one
        diff_h = (diff // 3600)
        diff_m = ((diff % 3600) // 60)
        diff_s = ((diff % 3600) % 60)
        s = ""
        if diff_h != 0:
            s += str(diff_h) + "ساعت"
        if diff_m != 0:
            if diff_h != 0:
                s += " و "
            s += str(diff_m) + "دقیقه"
        if len(arr2) == 3:
            if diff_s != 0:
                if s != "":
                    s += " و "
                s += str(diff_s) + "ثانیه"
        if diff_s <= 0 and diff_m <= 0 and diff_h <= 0:
            s += " 0 دقیقه"
        return s

    def __str__(self):
        return self.title;


class MyUserManager(BaseUserManager):
    def create_user(self, email,avatar = "static/blog/image/anynom.jpg" ,  name = "ناشناس", phone= "", password=None ):
        if not email:
            raise ValueError('وارد کردن ایمیل ضروری است!')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            name = name,
            phone = phone,
            avatar = avatar,
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
    email = models.EmailField(max_length=254, unique=True, db_index=True , null=False , blank=False)
    name = models.CharField(max_length=50 , default="ناشناس" , null=True, blank=True)
    phone = models.CharField(max_length=50 , default="0" , null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

