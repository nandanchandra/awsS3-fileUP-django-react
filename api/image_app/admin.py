from django.contrib import admin
# Register your models here.
from api.image_app.models import Imageaws

class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

admin.site.register(Imageaws,ImageAdmin)
