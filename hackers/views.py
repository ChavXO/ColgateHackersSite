from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost, Events


def index(request):
	template = loader.get_template('index.html')
	return render(request, 'index.html', {})

def blog_index(request):
    latest_post_list = BlogPost.objects.all()[:5]
    context = {'latest_blog_list':latest_post_list}
    template = loader.get_template('posts.html')
    return render(request, 'posts.html', context)
    
def blog_detail(request, post_id):
    post = ""
    try:
        post = BlogPost.objects.get(pk=post_id)
    except BlogPost.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'posts/detail.html', {'post': post})
    
def event_detail(request, event_id):
	latest_events_list = Events.objects[:5]
	context = {'latest_events_list':latest_events_list}
	template = loader.get_template('events.html')
	return render(request, 'events.html', context)

def event_index(request):
	latest_events_list = Events.objects.all()[:5]
	context = {'latest_events_list':latest_events_list}
	template = loader.get_template('events.html')
	return render(request, 'events.html', context)