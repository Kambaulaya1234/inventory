from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import auth
from django.contrib.auth.models import  User
from .models import Profile
from django.contrib import messages
from django.views import View
from .forms import ProfileForm
from django.conf import settings


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:       
            auth.login(request,user)
            messages.success(request,'Login successfully!')
            return redirect('base:home')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')


def register(request):
    if request.method=='POST':
            firstname=request.POST['fname']
            lastname=request.POST['lname']
            gender=request.POST['gender']
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            confirm_password=request.POST['cpassword']
            if password==confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.error(request,'Username Already exist ')
                    return redirect('register')       
                else:
                    if User.objects.filter(email=email).exists():
                         messages.error(request,'Email Already exist ')
                         return redirect('register')
                    else:
                            user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                            auth.login(request,user)
                            messages.success(request,'login successfully!')
                            if gender=='1':
                                my_status='Mr'                           
                                Profile.objects.create(user_id=request.user.id, profile='images/users/default/he.png',status=my_status)
                                return redirect('home')

                            elif gender=='2':
                                my_status='Miss'
                                Profile.objects.create(user_id=request.user.id, profile='images/users/default/she.png',status=my_status)
                                return redirect('base:home')
                            
                            
                     
            else:
                messages.error(request,"Password doesn't match")
                return redirect('register')
    else:
        return render(request,'accounts/register.html')


def logout(request):
        auth.logout(request)
        return redirect('login')



class Profile(View):
    template_name='accounts/profile.html'
    def get(self,*args,**kwargs):
        if not self.request.user.is_authenticated:
          messages.error(self.request,'Please Login first')
          return redirect(f'/{settings.LOGIN_URL}?next={self.request.path}')
        form=ProfileForm(instance=self.request.user.profile)
        context={
            'form':form
        }
        return render(self.request,self.template_name,context)

    def post(self,*args,**kwargs):
        form=ProfileForm(self.request.POST or None,self.request.FILES or None)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=self.request.user
            obj.save()
        messages.success(self.request,'Profile Updated successfully!')
        return redirect('profile')


def reset(request):
    if request.method=='POST':
        old_password=request.POST['old']
        new_password=request.POST['new']
        confirm_password=request.POST['confirm']
        print(new_password)
        print(confirm_password)
        if User.objects.filter(username=request.user.username).exists():
            if new_password == confirm_password:
                    user = auth.authenticate(username=request.user.username, password=old_password)
                    if user is not None:
                        username_only=User.objects.get(username=request.user.username)
                        username_only.set_password(confirm_password)
                        username_only.save()
                        messages.success(request,'Password Reset Successfully!')
                        return redirect('login')
                    else:
                        messages.error(request,"Username password doesn't exist !" )
                        return redirect('login')
            else:
                messages.error(request,"new password doesn't match !" )
                return redirect('reset')
        else:
            messages.error(request,"Username doesn't exist !" )
            return redirect('reset')
    else:
        return render(request,'accounts/reset.html')





      