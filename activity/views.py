from django.shortcuts import render,redirect
from django.views import View
from .models import Activity
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required,permission_required
from .forms import ActivityForm
from datetime import datetime,timedelta
from notifications.signals import notify
import nexmo
import threading
from django.conf import settings
User=settings.AUTH_USER_MODEL
from time import sleep


class SMSThread(threading.Thread):
    def __init__(self,body,delay):
        threading.Thread.__init__(self)
        self.delay=delay
        self.body=body
    def run(self):
        sleep(self.delay)
        print(self.body)
        # client = nexmo.Client(key='db9c6699', secret='gvTb1hDb8k8G5l1q')
        # client.send_message({
        #         'from': 'INVENTORY SYSTEM',
        #         'to': '255766325339',
        #         'text': self.body
        #     })

class SMSDeadlineThread(threading.Thread):
    def __init__(self,body,delay):
        threading.Thread.__init__(self)
        self.delay=delay
        self.body=body
    def run(self):
        sleep(self.delay)
        print(self.body)
        # client = nexmo.Client(key='db9c6699', secret='gvTb1hDb8k8G5l1q')
        # client.send_message({
        #         'from': 'INVENTORY SYSTEM',
        #         'to': '255766325339',
        #         'text': self.body
        #     })
     

class Index(LoginRequiredMixin,View):
    def get(self,request):
        template_name='activity/activity.html'
        activities = Activity.objects.order_by('-start_time')
        
        InitialData={
            'start_time':datetime.now(),
            'end_time':datetime.now() + timedelta(seconds=120),
        }
        form=ActivityForm(initial=InitialData)
        context={
            'activities':activities,
            'form':form,
        }
        
        return render(request,template_name,context)

    # permission_required = 'activity.add_activity'
    def post(self,request): 
        form=ActivityForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            object=form.save(commit=False)
            guard=object.guard
            object.save()
# ===============================================================================
            # timeFormat='%H:%M'
            # now=datetime.now().time().strftime(timeFormat)
            # deadline=guard.end_time.time().strftime(timeFormat)
            
            # time_now=datetime.strptime(f'{now}',timeFormat) 
            # time_deadline=datetime.strptime(f'{deadline}',timeFormat) 

            # delta=time_deadline-time_now
            # print('seeeeeeeeeeeeeeeeeeeeeeeeeeeeeconds',delta.seconds)



            body_text_t1=f'Hello Mr  {object.guard} you have new activity'
            body_text_t2=f'Hello Mr  {object.guard} you have to return weapon soon '
            startThread=SMSThread(body=body_text_t1,delay=1)
            startThread.start()
            deadlineThread=SMSDeadlineThread(body=body_text_t2,delay=60)
            deadlineThread.start()
# ===============================================================================

            notify.send(request.user,recipient=[guard],verb='You have been assigned new activity, you may login into your account to see it')

            messages.success(request,'activity created successfull!')
        return redirect('activity:index')

    




class Update(LoginRequiredMixin,View):
    permission_required = 'activity.change_activity'
    def post(self,request,*args,**kwargs):
            id_activity=kwargs['id']
            activity=Activity.objects.filter(id=id_activity)[0]
            form=ActivityForm(request.POST or None,request.FILES or None,instance=activity)
            if form.is_valid():
                form.save()
                messages.success(request,'activity updated successfull!')
                return redirect('activity:index')
            else:
                print(form.errors)
                return redirect('activity:index')

                
@login_required
@permission_required('activity.delete_activity')
def delete_activity(request,id):
    activity=Activity.objects.filter(id=id)[0] 
    activity.delete()
    messages.success(request,'activity deleted successfull!')
    return redirect('activity:index')


@login_required
@permission_required('activity.change_activity')
def verify(request,id,*args):
    activity=Activity.objects.filter(id=id)
    if (activity[0].status == False):
        activity.update(status=True)
        messages.success(request,f'Return of {activity[0].weapon} Verified successfull!')
        return redirect('activity:index')
    else:
       activity.update(status=False)
       messages.success(request,f'{activity[0].weapon} Return to Unverified state successfull!')
       return redirect('activity:index')


@login_required
def search(request):
    results=request.GET['search']
    template_name='activity/activity.html'
    activities = Activity.objects.filter(guard__username__icontains=results)
    context={
        'activities':activities,
    }
    
    return render(request,template_name,context)