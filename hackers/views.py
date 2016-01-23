from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('index.html')
	return render(request, 'index.html', {})

    
def blog_detail(request, post_id):
    response = "You are looking blog post %s."
    return HttpResponse(response % post_id)
    
def event_detail(request, event_id):
    response = "You are looking event post %s."
    return HttpResponse(response % event_id)

