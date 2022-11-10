from django.contrib import admin
from api.image_app.models import Imageaws
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

admin.site.register(Imageaws,ImageAdmin)
