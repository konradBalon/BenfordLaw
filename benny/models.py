from django.db import models

# Create your models here.
import config.settings


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True, default='myFile')
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
