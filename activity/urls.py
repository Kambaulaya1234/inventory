from django.urls import path
from .views import *

app_name='activity'

urlpatterns = [
    path('index/',Index.as_view(),name='index' ),
    path('<int:id>/',delete_activity,name='delete' ),
    path('update/<int:id>/',Update.as_view(),name='update' ),
    path('verify/<int:id>/',verify,name='verify' ),
    path('search/',search,name='search' ),

   
   

]