from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.showJobs, name='showJobs'),
    url(r'^$', views.home, name='home'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^add$', views.addingTask , name='addingTask'),
    url(r'^[\w\+%_& ]+/add$', views.addingTask , name='addingTask'),
    url(r'^addjob$', views.add_new_task , name='addingTask'),
    url(r'^upload_file$', views.upload_file , name='upload_file'),
    url(r'^[\w\+%_& ]+/addjob$', views.add_new_task , name='addingTask'),
    url(r'^(?P<pk2>\d+)/finish_task/(?P<pk>\d+)$', views.finish_task , name='finish_task'),
    # url(r'^logout/$', views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    # url(r'^login/$', views.login, {'template_name': 'login.html'}, name='login'),

    # url(r'admin/profile',  views.add_new_task , name='addingTask')


]
