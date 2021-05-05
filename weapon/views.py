from django.shortcuts import render,redirect
from django.views import View
from .models import Weapon
from django.contrib import messages
from .forms import WeaponForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required,permission_required
from datetime import datetime

class Index(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'weapon.view_weapon'
    def get(self,request):
        weapons=Weapon.objects.all()
        form=WeaponForm()
        context={
            'weapons':weapons,
            'form':form,
        }
       
        return render(request,'weapons/weapon_index.html',context)

    def post(self,request):
       
        form=WeaponForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            print(form)
        messages.success(request,'weapon created successfull!')
        return redirect('weapons_index')

class Update(LoginRequiredMixin,View):
    permission_required = 'weapon.change_weapon'
    def post(self,request,*args,**kwargs):
            id_weapon=kwargs['id']
            weapon=Weapon.objects.filter(id=id_weapon)[0]
            form=WeaponForm(request.POST or None,request.FILES or None,instance=weapon)
            if form.is_valid():
                form.save()
                messages.success(request,'weapon updated successfull!')
            return redirect('weapons_index')

@login_required
@permission_required('weapon.delete_weapons')
def delete_weapon(request,id):
    weapon=Weapon.objects.filter(id=id)[0]
    weapon.delete()
    messages.success(request,'weapon deleted successfull!')
    return redirect('../')