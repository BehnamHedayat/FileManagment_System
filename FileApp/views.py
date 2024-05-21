
from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from .models import Folder,File
from .forms import FolderForm,FileForm
from django.contrib.auth.decorators import login_required

@login_required
def Folders(request):
    
    user = request.user
    Folders = Folder.objects.filter(user=user)
   


    
    return render(request,"FileApp/Folders.html", {"Folders": Folders })



def Files(request, id):
    selected_Folder = Folder.objects.get(id=id)
    Files = selected_Folder.Files 
    context = {
        "selected_Folder": selected_Folder,
        "Files": Files,
    }
    return render(request,"FileApp/Files.html",context)  

@login_required
def CreateFolder(request):
    form = FolderForm()
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()    
            return render(request,"FileApp/CreateFolder.html", {"form": form })  
    return render(request,"FileApp/CreateFolder.html",{"form":form})


def UploadFile(request):
    form = FileForm()
    if request.method == "POST":
        form = FileForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request,"FileApp/UploadFile.html",{"form":form})

    return render (request,"FileApp/UploadFile.html",{"form":form})                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                  