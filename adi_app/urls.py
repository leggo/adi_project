from django.conf.urls import patterns, url
from adi_app import views

urlpatterns = patterns ('',
		url(r'^$', views.IndexView.as_view(), name='index'),
		url(r'^time/$', views.time, name='time'),
		url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='question'),
		url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
		url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
)