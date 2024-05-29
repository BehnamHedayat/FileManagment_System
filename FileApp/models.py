from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
import os
# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.user}"


class File(models.Model):
    name = models.CharField(max_length=100)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='Files')
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return f"{self.name} {self.folder}"

    @property
    def file_size(self):
        if self.file:
            return f"{self.file.size} bytes"
        return "No file"

    def file_size_human_readable(self):
        if self.file:
            size = self.file.size
            for unit in ['bytes','kb','mb','gb','tb']:
                if size < 1024:
                    return f"{size:.2f} {unit}"
                size /= 1024.0
        return "No file"
