
from re import template
from django.urls import path,include
from .views import Folders,Files,CreateFolder, UploadFile,Index
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('', auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
   path('logout/', auth_views.LoginView.as_view(),name='logout'),
   path('folders',Folders, name='folders'),
   path('<int:id>/',Files,name='file'),
   path('create',CreateFolder,name='creatfolder'),
   path('upload',UploadFile,name='uploadfile')

]