
from django import forms
from .models import Folder, File
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name','file']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']