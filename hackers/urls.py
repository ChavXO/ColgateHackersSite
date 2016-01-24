from django.conf.urls import url

from . import views

app_name = 'hackers'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/(?P<event_id>[0-9]+)/$', views.event_detail, name='event_detail'),
    url(r'^posts/$', views.blog_index, name='blog_index'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.blog_detail, name='blog_details'),
	url(r'^events/$', views.event_index, name = 'event_index'),
]