from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<event_id>[0-9]+)/$', views.event_detail, name='event_detail'),
    url(r'^(?P<post_id>[0-9]+)/$', views.blog_detail, name='blog_detail'),
    
]