
# Register your models here.

from django.contrib import admin
from .models import WorkBox, MyUser, MyUserManager
from .models import Work


admin.site.register(WorkBox)
admin.site.register(Work)
admin.site.register(MyUser)
# admin.site.register(MyUserManager)

