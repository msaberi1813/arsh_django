
# Create your models here.
from django.db import models
from django.utils import timezone
from time import gmtime, strftime
from datetime import datetime


class WorkBox(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())



class Work(models.Model):

    title = models.CharField(max_length=30 , null=False , default="کار");
    beginnig_time = models.TimeField(default = timezone.now())
    finish_time = models.TimeField(default = None , null=True);
    workbox = models.ForeignKey(WorkBox, on_delete=models.CASCADE)
    isFinished = models.BooleanField(default= False)
    # shour =  - beginnig_time
    # sh = datetime.date.today().strftime("%H")
    # fh = finish_time.strftime("%Y")
    def duration(self):
        diff= self.finish_time - self.beginnig_time
        duration = (diff.days * 86400000) + (diff.seconds * 1000) + (diff.microseconds / 1000)


    def __str__(self):
        return self.title;

