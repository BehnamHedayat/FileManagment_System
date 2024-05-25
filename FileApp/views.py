
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from .models import Folder,File
from .forms import FolderForm,FileForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

@login_required
def Folders(request):
    
    user = request.user
    Folders = Folder.objects.filter(user=user)
   


    
    return render(request,"FileApp/Folders.html", {"Folders": Folders })


@login_required
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
            form = FolderForm()
            user = request.user
            Folders = Folder.objects.filter(user=user)    
            return render(request,"FileApp/Folders.html", {"Folders": Folders })
      
    return render(request,"FileApp/CreateFolder.html",{"form":form})

@login_required
def UploadFile(request, folder_id):
    form = FileForm()
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            folder = Folder.objects.get(id=folder_id)
            form.instance.folder = folder
            form.save()
            
            return render (request,"FileApp/UploadFile.html",{"form":form})

    return render (request,"FileApp/UploadFile.html",{"form":form})  

@login_required
def Index(request):
    return render(request, 'index.html')  

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return  redirect('Folders') 
    else:
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {"form":form})                                                                                                                            
                                                                                                                                                                                                                                                                                                                                  