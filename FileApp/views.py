from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse
from .models import Folder,File

def Folders(request):
    user = request.user
    Folders = Folder.objects.filter(user=user)
    context = {
        "Folders": Folders
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
                                                                                                                                                                                                                                                                                                                                  