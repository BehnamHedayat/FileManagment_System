
from django.urls import path
from .views import Folders,Files,CreateFolder, UploadFile


urlpatterns = [
   path('',Folders),
   path('<int:id>/',Files,name='file'),
   path('create',CreateFolder,name='creatfolder'),
   path('upload',UploadFile,name='uploadfile')

]