from django.db import models

# Create your models here.

class Imageaws(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(blank=False, null=False, upload_to='image')