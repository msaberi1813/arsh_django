import time

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.utils import timezone
from .models import WorkBox, Work, MyUser, MyUserManager
from .forms import NameForm , UploadFileForm
from django.shortcuts import render, render_to_response
from django.core.files.storage import FileSystemStorage
from .duration import duration2
# Create your views here.

@login_required(redirect_field_name='login')
def home(request):
    user = MyUser.objects.filter(pk = request.user.pk)
    boxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
    return render(request, 'blog/test2.html', {'workboxes': boxes})

def showJobs(request, pk):
    workboxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
    myworkbox = WorkBox.objects.get(author=request.user ,  pk=pk)
    works=Work.objects.filter(workbox=myworkbox)

    return render(request, 'blog/test2.html', {'works':works,'workboxes':workboxes, 'pkey' : pk} )

#
def addingTask(request):
    # pass
    if request.method == 'POST':
        newBox = WorkBox.objects.create(author=request.user)
        url = reverse('showJobs', kwargs={'pk': newBox.pk})
        return HttpResponseRedirect(url)

def add_new_task(request  ):

    if request.method == 'POST':
        form = NameForm(request.POST)
        p=form.data['pk']
        q= WorkBox.objects.get(pk=int(form.data['pk']))
        recentJobs = Work.objects.filter(workbox=q)

        print(recentJobs)
        for element in recentJobs:
            if element.finish_time is None:
               element.finish_time = timezone.now()
               element.save()
        before = Work.objects.filter( workbox = q).last()
        if before is not None:
            # print(form.data['pk'])
            if (before.isFinished == False):
                before.isFinished=True
                before.finish_time = str(time.strftime("%H:%M"))
                before.d = duration2(before.beginnig_time, str(time.strftime("%H:%M")))
                before.save()
                print(before.beginnig_time)
        newjob = Work.objects.create(title=form.data['title'], workbox= WorkBox.objects.get(pk=int(form.data['pk'])))
        workboxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
        myworkbox = WorkBox.objects.get(author=request.user, pk=int(form.data['pk']))

        works = Work.objects.filter(workbox=myworkbox)
    else:
        newjob = None

    return render(request, 'blog/test2.html', {'works': works, 'workboxes': workboxes, 'newjob': newjob , 'pkey':form.data['pk'] })

def finish_task(request , pk ,pk2):
    form_class = NameForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        print("ggggggggggggggggggggggggggggggg")
        w = Work.objects.filter(pk = pk).first()
        w.finish_time = str(time.strftime("%H:%M"))
        print(w.finish_time)
        w.d = duration2( w.beginnig_time , str(time.strftime("%H:%M")))
        x=WorkBox.objects.get(pk=pk2)
        newjo = Work.objects.create( workbox=WorkBox.objects.get(pk=int(form.data['pk'])))
        workboxe = WorkBox.objects.filter(author=request.user).order_by('created_date')


    return render(request, 'blog/test2.html',   {'workboxes': workboxe , 'newjob': newjo , 'pkey':form.data['pk'] })


def profile(request):
    return render (request , 'blog/test.html' , {})



def upload_file(request):

    form_class = NameForm
    form = form_class(request.POST, request.FILES)
    if request.method == 'POST' :
        # myfil= None
        if form.is_valid():
            try:
             user = MyUser.objects.create_user(name=form.data['name'], email=form.data['email'],  phone=form.data['phone'], password=form.data['password'])
            except:
                messages.error(request, 'وارد کردن ایمیل غیر تکراری ضروری است')
            else:

                if 'myfile' in request.FILES:
                    myfil = request.FILES['myfile']
                    fs = FileSystemStorage()
                    filename = fs.save(myfil.name, myfil)
                    uploaded_file_url = fs.url(filename)
                    print("yeeeeeeeeeeeeeeeeeeeeeeeeeeeees")
                    user.avatar = uploaded_file_url
                    user.save()
                else:
                    uploaded_file_url = "static/blog/image/anynom.jpg"

                    messages.success(request, 'ثبت نام با موفقیت انجام شد')

                return render(request, 'blog/test.html', {
                    'uploaded_file_url': uploaded_file_url , 'user':user
                })
    return render(request, 'blog/test.html')




        # try:
        # except:
        #     user.avatar = 'static/blog/image/anynom.jpg'
        # messages.success(request, 'ثبت نام با موفقیت انجام شد')
        #

