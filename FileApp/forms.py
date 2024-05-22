
from dataclasses import field
from django import forms
from .models import Folder, File


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name','folder','file']