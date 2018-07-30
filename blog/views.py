from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect
from django.urls import reverse
from .models import WorkBox, Work, MyUser
from .forms import NameForm
from django.shortcuts import render
from .duration import duration2
from khayyam import *


@login_required(redirect_field_name='login')
def home(request):
    boxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
    return render(request, 'blog/test3.html', {'workboxes': boxes})

def showJobs(request, pk):
    workboxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
    myworkbox = WorkBox.objects.get(author=request.user ,  pk=pk)
    works=Work.objects.filter(workbox=myworkbox)

    return render(request, 'blog/test2.html', {'works':works,'workboxes':workboxes, 'pkey' : pk} )

def addingTask(request):
    if request.method == 'POST':
        newBox = WorkBox.objects.create(author=request.user , title=str(JalaliDatetime.now().strftime('%C')))
        url = reverse('showJobs', kwargs={'pk': newBox.pk})
        return HttpResponseRedirect(url)

def add_new_task(request  ):

    if request.method == 'POST':
        form = NameForm(request.POST)
        p = form.data['pk']

        try:
            q = WorkBox.objects.get(pk=form.data['pk'])
        except:
            print(form.data['pk'])
            q = WorkBox.objects.create(pk=1)
        recentJobs = Work.objects.filter(workbox=q)
        for element in recentJobs:
            if element.finish_time == "":
               element.finish_time =  JalaliDatetime.now().strftime('%H:%M:%S')
               element.save()
        before = Work.objects.filter( workbox = q).last()
        if before is not None:
            if (before.isFinished == False):
                before.isFinished=True
                before.finish_time = JalaliDatetime.now().strftime('%H:%M:%S')
                before.d = duration2(str(before.beginnig_time),str( JalaliDatetime.now().strftime('%H:%M:%S')))
                before.save()
                print(before.beginnig_time)
        newjob = Work.objects.create(title=form.data['title'], workbox= WorkBox.objects.get(pk=int(form.data['pk'])), beginnig_time = (JalaliDatetime.now().strftime('%H:%M:%S')))
        workboxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
        works = Work.objects.filter(workbox=q)
    else:
        newjob = None
    return render(request, 'blog/test2.html', {'works': works, 'workboxes': workboxes, 'newjob': newjob , 'pkey':p })

def finish_task(request , pk2 ,pk3):
    if request.method == 'POST':
        w = Work.objects.filter(pk = pk3).first()
        w.finish_time = JalaliDatetime.now().strftime('%H:%M:%S')
        print(w.finish_time)
        w.d = duration2(str( w.beginnig_time ),str( JalaliDatetime.now().strftime('%H:%M:%S')))
        w.save()
        workboxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
        myworkbox = workboxes.get( pk=pk2)
        works = Work.objects.filter(workbox=myworkbox)

    return render(request, 'blog/test2.html',   {'works': works,'workboxes': workboxes ,  'pkey':pk2 })


def profile(request):
    f=NameForm()
    return render (request , 'blog/test.html' , {'form':f})



def upload_file(request):
    form = NameForm(request.POST, request.FILES)
    if request.method == 'POST' :
        if form.is_valid():
                user = MyUser.objects.create_user(name=form.data['name'], email=form.data['email'],  phone=form.data['phone'], password=form.data['password'])
                messages.success(request, 'ثبت نام با موفقیت انجام شد')
                if form.cleaned_data['avatar'] is not None:
                     print(form.cleaned_data['avatar'])
                     user.avatar = form.cleaned_data['avatar']
                else:
                    user.avatar = "static/blog/image/anynom.jpg"
                print(user.avatar)
                user.save();
                return render(request, 'blog/test.html', { 'user':user
                })
    return render(request, 'blog/test.html', {'form':form})



