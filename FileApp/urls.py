
from django.urls import path
from .views import Folders,Files,CreateFolder 


urlpatterns = [
   path('',Folders),
   path('<int:id>/',Files,name='file'),
   path('create',CreateFolder,name='creatfolder')
]