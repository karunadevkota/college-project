from django.shortcuts import render,redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from myapp.models import Profile, News,Record,Case_Study,Report,Contact
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail

from django.http import HttpResponse,JsonResponse, HttpResponseRedirect

# Create your views here.

#index
def index(request):
    case=Case_Study.objects.all()
    context ={'case':case}
    if request.method=="POST":
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        obj=Contact(email=email,message=message)
        obj.save()
    
    return render(request,'index.html',context)

#about 
def about(request):
    if request.method=="POST":
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        obj=Contact(email=email,message=message)
        obj.save()
    return render(request,'about.html')

#report crime

def report(request):    
    context={}
    if request.method=="POST":
       
        #fetch data from html form
        crimetype=request.POST.get('crimetype')
        victimname = request.POST.get('victimname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        reportingperson = request.POST.get('reportingperson')
        incidentdate=request.POST.get('incidentdate')
        incidentlocation= request.POST.get('incidentlocation')
        description= request.POST.get('description')
        no_of_people= request.POST.get('no_of_people')
        affected=request.POST.get('affected')
     
        obj=Report(crimetype=crimetype,victimname=victimname,email=email,phonenumber=phonenumber,reportingperson=reportingperson,incidentdate=incidentdate, incidentlocation=incidentlocation,description=description, no_of_people=no_of_people,affected=affected)
        obj.save()
    return render(request,'report.html', context)



# news 
def news(request):
    news=News.objects.all()
    context ={'news':news}
    return render(request,'news.html',context)

#criminal records
def record(request):
    record=Record.objects.all()
    context ={'record':record}
    return render(request,'record.html',context)

#emergency contact number
def econtact(request):
    return render(request,'econtact.html')

# police station 
def station(request):
    return render(request,'station.html')

#register
def register(request):
        
    context={}
    if request.method=="POST":
        #fetch data from html form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        contact = request.POST.get('number')
        check = User.objects.filter(username=email)
        if len(check)==0:
            #Save data to both tables
            usr = User.objects.create_user(email, email, password)
            usr.first_name = name
            usr.save()
            profile = Profile(user=usr, contact_number = contact)
            profile.save()
            context['status'] = f"User {name} Registered Successfully!"
        else:
            context['error'] = f"A User with this email already exists"
      
    return render(request,'register.html', context)

#check validation
def check_user_exists(request):
    email = request.GET.get('usern')
    check = User.objects.filter(username=email)
    if len(check)==0:
      return JsonResponse({'status':0,'message':'Not Exist'})
    else:
        return JsonResponse({'status':1,'message':'A user with this email already exists!'})


#login
def signin(request):
   
        
    context={}
    if request.method=="POST":
        email = request.POST.get('email')
        passw = request.POST.get('password')
        check_user = authenticate(username=email, password=passw)
        if check_user:
            login(request, check_user)
            if check_user.is_superuser or check_user.is_staff:
                return HttpResponseRedirect('/admin')
            return HttpResponseRedirect('/dashboard') 
        else:
            context.update({'message':'Invalid Login Details!','class':'alert-danger'})     
    return render(request,'login.html', context)

#dashboard
def dashboard(request):
 
    context={}
    login_user = get_object_or_404(User, id = request.user.id)
    #fetch login user's details
    profile = Profile.objects.get(user__id=request.user.id)
    context['profile'] = profile

    #update profile
    if "update_profile" in request.POST:
        print("file=",request.FILES)
        name = request.POST.get('name')
        contact = request.POST.get('contact_number')
        add = request.POST.get('address')
       

        profile.user.first_name = name 
        profile.user.save()
        profile.contact_number = contact 
        profile.address = add 

        if "profile_pic" in request.FILES:
            pic = request.FILES['profile_pic']
            profile.profile_pic = pic
        profile.save()
        context['status'] = 'Profile updated successfully!'
    
    #Change Password 
    if "change_pass" in request.POST:
        c_password = request.POST.get('current_password')
        n_password = request.POST.get('new_password')

        check = login_user.check_password(c_password)
        if check==True:
            login_user.set_password(n_password)
            login_user.save()
            login(request, login_user)
            context['status'] = 'Password Updated Successfully!' 
        else:
            context['status'] = 'Current Password Incorrect!'

    
      
    return render(request, 'dashboard.html', context)

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')   

