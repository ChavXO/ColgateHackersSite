from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost, Events


def index(request):
	template = loader.get_template('index.html')
	return render(request, 'index.html', {})

    
def blog_detail(request, post_id):
	latest_post_list = BlogPost.objects[:5]
	context = {'latest_blog_list':latest_post_list}
	template = loader.get_template('blog.html')
	return render(request, 'post.html', context)
    
def event_detail(request, event_id):
	latest_events_list = Events.objects[:5]
	context = {'latest_events_list':latest_events_list}
	template = loader.get_template('events.html')
	return render(request, 'events.html', context)
