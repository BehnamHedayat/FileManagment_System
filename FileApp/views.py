
from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from .models import Folder,File
from .forms import FolderForm
from django.contrib.auth.decorators import login_required

@login_required
def Folders(request):
    form = FolderForm()
    user = request.user
    Folders = Folder.objects.filter(user=user)
   
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            
            form.instance.user = request.user
            form.save()    
            return render(request,"FileApp/Folders.html", {"Folders": Folders,"form": form })

    
    return render(request,"FileApp/Folders.html", {"Folders": Folders,"form": form })



def Files(request, id):
    selected_Folder = Folder.objects.get(id=id)
    Files = selected_Folder.Files 
    context = {
        "selected_Folder": selected_Folder,
        "Files": Files,
    }
    return render(request,"FileApp/Files.html",context)    

                                                                                                                                           
                                                                                                                                                                                                                                                                                                                                  