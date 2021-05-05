from django.urls import path
from .views import *


app_name='tracking'
urlpatterns = [
    path('',Index.as_view(),name='index'),

]