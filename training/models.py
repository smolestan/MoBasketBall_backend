from django.db import models

class Training(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    video = models.FileField(upload_to='vids', blank=True, null=True)