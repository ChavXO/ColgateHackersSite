from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def blog_detail(request, post_id):
    response = "You are looking blog post %s."
    return HttpResponse(response % post_id)
    
def event_detail(request, event_id):
    response = "You are looking event post %s."
    return HttpResponse(response % event_id)

