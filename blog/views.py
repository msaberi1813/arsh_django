from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from .models import WorkBox, Work
from .forms import NameForm

# Create your views here.
def home(request):
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
        newBox = WorkBox.objects.create(author = request.user)
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
        newjob = Work.objects.create(title=form.data['title'], workbox= WorkBox.objects.get(pk=int(form.data['pk'])))
        workboxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
        myworkbox = WorkBox.objects.get(author=request.user, pk=int(form.data['pk']))
        works = Work.objects.filter(workbox=myworkbox)
    else:
        newjob = None

    return render(request, 'blog/test2.html', {'works': works, 'workboxes': workboxes, 'newjob': newjob , 'pkey':form.data['pk']})





