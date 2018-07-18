from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from .models import WorkBox, Work, MyUser, MyUserManager
from .forms import NameForm , UploadFileForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .somewhere import handle_uploaded_file
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
                before.finish_time = timezone.now()
                before.save()
                print(before.beginnig_time)
        newjob = Work.objects.create(title=form.data['title'], workbox= WorkBox.objects.get(pk=int(form.data['pk'])))
        workboxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
        myworkbox = WorkBox.objects.get(author=request.user, pk=int(form.data['pk']))
        works = Work.objects.filter(workbox=myworkbox)
    else:
        newjob = None

    return render(request, 'blog/test2.html', {'works': works, 'workboxes': workboxes, 'newjob': newjob , 'pkey':form.data['pk']})

def finish_task(request , pk ,pk2):
    form_class = NameForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'post':
        w = Work.objects.filter(pk = form.data['pk'])
        w.finish_time = timezone.now()

        newjob = Work.objects.create(title=form.data['title'], workbox=WorkBox.objects.get(pk=int(form.data['pk2'])))
        workboxes = WorkBox.objects.filter(author=request.user).order_by('created_date')
        myworkbox = WorkBox.objects.get( pk=form.data['pk2'])
        works = Work.objects.filter(pk2=myworkbox.pk)
    return render(request, 'blog/test2.html',  { 'workboxes': workboxes, 'newjob': newjob, 'pkey': form.data['pk']})

# def login(request):


def profile(request):
    return render (request , 'blog/test.html' , {})

def register(request , image , email , passw):
    u = MyUser.objects.create_user(email, passw)
def simple_upload(request):
    myfile = None
    form_class = NameForm
    form = form_class(request.POST or None)
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'blog/test.html', {
            'uploaded_file_url': uploaded_file_url
        })
    url = reverse('register', kwargs={'image' : myfile , 'email': form.data['email'] , 'passw':form.data['pass']})
    return HttpResponseRedirect(url)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        handle_uploaded_file(request.FILES['file'])
        url = reverse('register', kwargs={'image': request.FILES['file'], 'email': form.data['email'], 'passw': form.data['pass']})
        return HttpResponseRedirect(url)
    else:
        form = UploadFileForm()
    return render(request, 'blog/test.html', {'form': form})