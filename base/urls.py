from django.urls import path,include
from .views import *


app_name='base'
urlpatterns=[
    path('',NormalDashboard.as_view() ,name='home'),
    path('normal-dashboard/',NormalDashboard.as_view() ,name='normal_dashboard'),
    path('admin-dashboard',AdminDashboard.as_view() ,name='admin_dashboard'),
]