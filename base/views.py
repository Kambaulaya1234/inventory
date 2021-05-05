from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from activity.models import Activity
from systemsite.models import SiteSystem
from weapon.models import Weapon
from django.contrib.auth.models import User

from django.db.models import Count,Sum



class Index(LoginRequiredMixin,View):
    def get(self,request):
        template_name='index.html'
        return render(request,template_name)
        
class NormalDashboard(LoginRequiredMixin,View):
    def get(self,request):
        template_name='normal_dashboard.html'
        user_activities = Activity.objects.order_by('-start_time')
        user_activities = Activity.objects.filter(guard=self.request.user).order_by('-start_time')
        context={
            'activities':user_activities,
        }
        return render(request,template_name,context)

class AdminDashboard(LoginRequiredMixin,View):
    def get(self,request):
        template_name='admin_dashboard.html'
        activities = Activity.objects.filter(status=False).order_by('-start_time')
        users = User.objects.all()
        sites = SiteSystem.objects.all()
        weapons_all = Weapon.objects.aggregate(weapons_counts=Sum('total'))
        if weapons_all['weapons_counts'] == None:
            weapons_all['weapons_counts']=0
            weapons_remained =int(weapons_all['weapons_counts'])
        else:
            weapons_remained =int(weapons_all['weapons_counts']) - activities.count()

        context={ 
            'users':users,
            'activities':activities,
            'sites':sites,
            'weapons':weapons_all['weapons_counts'],
            'weapons_remained':weapons_remained,
        }
        return render(request,template_name,context)

    