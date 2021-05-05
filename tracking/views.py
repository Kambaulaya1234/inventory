from django.shortcuts import render
from django.views import View
from activity.models import Activity
# Create your views here.
class Index(View):
    def get(self,*args,**kwargs):
        template_name='tracking/tracking_index.html'
        activities = Activity.objects.filter(status=False)
        context={
            'activities':activities
        }
        return render(self.request,template_name,context)