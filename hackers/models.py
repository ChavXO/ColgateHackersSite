from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title_text = models.CharField(max_length=50)
    article_text = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')
    
class Events(models.Model):
    event_name_text = models.CharField(max_length=50)
    event_detail_text = models.CharField(max_length=10000)
    event_creation_date = models.DateTimeField('date published')
    event_occurence_date = models.DateTimeField('Date of event')
    
