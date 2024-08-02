from django.contrib import admin 

from .models import Product, Screen ,PDFFile,VideoFile

# Register your models here.
admin.site.register(Product)
admin.site.register(Screen)
admin.site.register(VideoFile)
admin.site.register(PDFFile)