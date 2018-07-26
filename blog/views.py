import time
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import WorkBox, Work, MyUser
from .forms import NameForm
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .duration import duration2


@login_required(redirect_field_name='login')
def home(request):
    user = MyUser.objects.filter(pk = request.user.pk)
    boxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
    return render(request, 'blog/test3.html', {'workboxes': boxes})

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
               element.finish_time = timezone.now().time()
               element.save()
        before = Work.objects.filter( workbox = q).last()
        if before is not None:
            # print(form.data['pk'])
            if (before.isFinished == False):
                before.isFinished=True
                before.finish_time = timezone.now().time()
                before.d = duration2(str(before.beginnig_time),str(timezone.now().time()))
                # print("gggggggggggggggggggggggggggggggggggggggg",before.beginnig_time )
                before.save()
                print(before.beginnig_time)
        newjob = Work.objects.create(title=form.data['title'], workbox= WorkBox.objects.get(pk=int(form.data['pk'])))
        workboxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
        myworkbox = WorkBox.objects.get(author=request.user, pk=int(form.data['pk']))

        works = Work.objects.filter(workbox=myworkbox)
    else:
        newjob = None

    return render(request, 'blog/test2.html', {'works': works, 'workboxes': workboxes, 'newjob': newjob , 'pkey':form.data['pk'] })

def finish_task(request , pk2 ,pk):
    form_class = NameForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        w = Work.objects.filter(pk = pk).first()
        w.finish_time = timezone.now().time()
        print(w.finish_time)
        w.d = duration2(str( w.beginnig_time ),str(timezone.now().time()))
        w.save()
        newjob = Work.objects.create(workbox=WorkBox.objects.get(pk=pk2))
        workboxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
        myworkbox = workboxes.get( pk=pk2)
        works = Work.objects.filter(workbox=myworkbox)

    return render(request, 'blog/test2.html',   {'works': works,'workboxes': workboxes , 'newjob': newjob , 'pkey':pk })


def profile(request):
    f=NameForm()
    return render (request , 'blog/test.html' , {'form':f})



def upload_file(request):
    # print("ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
    # form_class = NameForm
    form = NameForm(request.POST, request.FILES)
    if request.method == 'POST' :
        # myfil= None
        if form.is_valid():
                user = MyUser.objects.create_user(name=form.data['name'], email=form.data['email'],  phone=form.data['phone'], password=form.data['password'])

            # else:
                s=1
                messages.success(request, 'ثبت نام با موفقیت انجام شد')
                # form.save()
                # if request.FILES is not None:
                if form.cleaned_data['avatar'] is not None:
                     print(form.cleaned_data['avatar'])
                     user.avatar = form.cleaned_data['avatar']
                     s=2

                user.save();
                #
                return render(request, 'blog/test.html', { 'user':user
                })
    return render(request, 'blog/test.html', {'form':form})



