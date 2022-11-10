from django.db import models
from api.utils.models import TimeStampedModel
from api.utils.image_utils import rename_image
# Create your models here.

class Imageaws(TimeStampedModel):
    title = models.CharField(max_length=30)
    document = models.FileField(blank=False, null=False, upload_to=rename_image)

    def __str__(self):
        return '%s - %s' % (self.id,self.title)
    class Meta:
        ordering = ('created_at',) 
        verbose_name_plural = 'Aws Image'