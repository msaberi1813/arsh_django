
# Register your models here.

from django.contrib import admin
from .models import WorkBox
from .models import Work


admin.site.register(WorkBox)
admin.site.register(Work)
