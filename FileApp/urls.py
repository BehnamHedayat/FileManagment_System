
from django.urls import path
from .views import Folders,Files 


urlpatterns = [
   path('',Folders),
   path('<int:id>/',Files,name='file')
]