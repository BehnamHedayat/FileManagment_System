
from re import template
from django.urls import path,include
from .views import Folders,Files,CreateFolder, UploadFile,register
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('', auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
   path('logout/', auth_views.LoginView.as_view(),name='logout'),
   path('register/', register, name='register'),
   path('folders',Folders, name='folders'),
   path('<int:id>/',Files,name='file'),
   path('create',CreateFolder,name='creatfolder'),
   path('upload/<int:folder_id>',UploadFile,name='uploadfile'),

]