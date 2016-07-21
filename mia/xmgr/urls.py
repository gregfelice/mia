from django.conf.urls import url

from . import views

app_name = 'xmgr'
urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /xmgr
    # url(r'^$', views.index, name='index'),
    
    # /xmgr/5/
    # url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),

]
