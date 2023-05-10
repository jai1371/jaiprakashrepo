import asyncio

from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import contactform,loginform,userchangeform
from .models import User,profile,student
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView,LogoutView
import uuid
from .emailverification import send_email_token
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

class studentlistview(ListView):
    model = student
    template_name = "ecommerceapp/templates/student.html"
class studentcreateview(CreateView):
    model = student
    template_name = "ecommerceapp/templates/studentcreate.html"
    fields = "__all__"
    success_url = '/student'
class studentdetailview(DetailView):
    model = student
    template_name = "ecommerceapp/templates/studentdetail.html"
    fields = "__all__"
class studentupdateview(UpdateView):
    model = student
    template_name = "ecommerceapp/templates/studentupdate.html"
    fields = "__all__"
    success_url = "/student"
class studentdeleteview(DeleteView):
    model = student
    template_name = "ecommerceapp/templates/studentdelete.html"
    success_url = "/student"

# accounts
x=[staff_member_required,login_required]
@method_decorator(x,name='dispatch')
class profiletemplateview(TemplateView):
    template_name = 'registration/profile.html'

class LogouttemplateView(TemplateView):
    template_name = 'registration/profile.html'

class PasswordChangetemplateView(TemplateView):
    template_name = 'registration/profile.html'



'''def contact(request):
    if request.method=='POST':
        form=contactform(request.POST)# this is new thing i have learn
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponse("successfully submitted")
        else:
            return render(request, 'contactform.html', {'form': form})
    return render(request,'contactform.html',{'form':contactform})
def userchange(request):
    if request.method=='POST':
        form=userchangeform(request.POST)# this is new thing i have learn
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponse("successfully submitted")
        else:
            return render(request, 'contactform.html', {'form': form})
    return render(request,'contactform.html',{'form':userchangeform})


# class registerform(CreateView):
#     template_name = 'contactform.html'
#     form_class = contactform
#     # fields = '__all__'
#     success_url = "/admin"
#
class loginformview(LoginView):
    template_name = 'contactform.html'
    form_class = loginform
    # fields = '__all__'
    success_url = "/admin"

def home(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user_obj=User(email=email)
        user_obj.set_password(password)
        user_obj.save()
        profile_obj=profile.objects.create(user=user_obj,
                            email_token=str(uuid.uuid4()))
        send_email_token(email=email,token=profile_obj.email_token)
        return HttpResponse("EMAIL SENT SUCCESSFULLY")
    return render(request,'home.html')
def verify(request,token):
    try:
        obj=profile.objects.get(email_token=token)
        obj.is_verified=True
        obj.save()
        return HttpResponse("email verified successfully")
    except Exception as e:
        return HttpResponse('invalid token')'''


#got eception signal related :

async def exception_signal(request):
    print("hello")
    await asyncio.sleep(5)          #seconds
    a=10/0
    return HttpResponse("exception done")


def school(request):
    return render(request,"school.html")