#from __future__ import unicode_literals
#import os

from django.conf import settings
#from django.utils import timezone
#from django.core.exceptions import ValidationError

from django.db import models

# Create your models here.
class WebsiteInfo(models.Model):
    page_name = models.CharField(max_length=40, default='Daydreaming in NYC')
    page_owner = models.CharField(max_length=20)
    page_message = models.TextField(max_length=500)
    page_message_author = models.CharField(max_length=30)
    page_info = models.TextField(max_length=1000)
    page_photo = models.ImageField(upload_to=settings.STATIC_ROOT+'image/website_info/')
    
    def __str__(self):
        return self.page_owner
        
    class Meta:
        db_table = 'website_info'
        verbose_name = 'Website Info'
        verbose_name_plural = 'Website Info'