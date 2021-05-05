from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from .views import *



urlpatterns = [
    path('',Index.as_view(),name='weapons_index' ),
    path('<int:id>/',delete_weapon,name='delete_weapon' ),
    path('update/<int:id>/',Update.as_view(),name='update_weapon' ),
   
   

]