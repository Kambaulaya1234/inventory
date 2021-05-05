from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from .views import *


app_name='systemsite'
urlpatterns = [
    path('',Index.as_view(),name='index' ),
    path('<int:id>/',delete_systemsite,name='delete'),
    path('update/<int:id>/',Update.as_view(),name='update')

]