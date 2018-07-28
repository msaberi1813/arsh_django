from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.showJobs, name='showJobs'),
    url(r'^$', views.home, name='home'),
    url(r'^profile$', views.profile, name='profile'),

    url(r'^add$', views.addingTask , name='addingTask'),
    url(r'^[\w\+%_& ]+/finish_task/add$', views.addingTask , name='addingTask'),
    url(r'^[\w\+%_& ]+/add$', views.addingTask , name='addingTask'),

    url(r'^[\w\+%_& ]+/addjob$', views.add_new_task, name='addjob'),
    url(r'^[\w\+%_& ]+/addjob/[\w\+%_& ]+$', views.add_new_task , name='addjob'),

    url(r'^(?P<pk2>\d+)/(?P<pk3>\d+)$', views.finish_task, name='finish_task'),

    url(r'^upload_file$', views.upload_file , name='upload_file'),

]

