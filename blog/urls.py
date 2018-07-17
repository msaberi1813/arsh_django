from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.showJobs, name='showJobs'),
    url(r'^$', views.home, name='Arsh_scheduling'),
    url(r'^add$', views.addingTask , name='addingTask'),
    url(r'^[\w\+%_& ]+/add$', views.addingTask , name='addingTask'),
    url(r'^addjob$', views.add_new_task , name='addingTask'),
    url(r'^[\w\+%_& ]+/addjob$', views.add_new_task , name='addingTask'),


]
