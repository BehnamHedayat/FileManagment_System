from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Folder, File


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ["name"]