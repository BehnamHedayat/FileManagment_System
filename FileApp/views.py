from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse
from .models import Folder,File
from .forms import FolderForm

def Folders(request):
    form = FolderForm()
    user = request.user
    if request.method == "post":
        form = FolderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            newFolder = Folder(name=name, user=user)
            newFolder.save()
    
    Folders = Folder.objects.filter(user=user)
    context = {
        "Folders": Folders,
        "form": form
    }
    return render(request,"FileApp/Folders.html", context)



def Files(request, id):
    selected_Folder = Folder.objects.get(id=id)
    Files = selected_Folder.Files 
    context = {
        "selected_Folder": selected_Folder,
        "Files": Files,
    }
    return render(request,"FileApp/Files.html",context)                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                  