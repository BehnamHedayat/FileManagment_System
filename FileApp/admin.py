from atexit import register
from django.contrib import admin
from .models import Folder, File

# Register your models here.
admin.site.register(Folder)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name','folder','file_size_human_readable')