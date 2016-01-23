from django.contrib import admin
from .models import BlogPost
from .models import Events

admin.site.register(BlogPost)
admin.site.register(Events)
