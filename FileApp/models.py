from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class File(models.Model):
    name = models.CharField(max_length=100)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='Files')
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return f"{self.name}"
