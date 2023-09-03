from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime

# Create your views here.


def home(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"course.html")

def contact(request):
    return render(request,"home.html")


def profile(request):
    return render(request,"login.html")
    

def reg(request):
    return render(request,"profile.html")

def reg(request):
    return render(request,"reg.html")
        
    






import hashlib
def ureg(request):
        uname=request.GET.get('renuka')
        pwd=request.GET.get('renu@17')
        pwd=hashlib.md5(pwd.encode('utf-8')).hexdigest()

        email=request.GET.get('email')
        gender=request.GET.get('gender')
        phone=request.GET.get('phone')
        print(uname,pwd,email,gender,phone)
        u=Customer(username=uname,pwd=pwd,email=email,gender=gender,pno=phone)
        u.save()
        return render(request,'login.html')
        
def login(request):
    return render(request, 'login.html')

def ulogin(request):
    uname=request.GET.get('username')
    pwd=request.GET.get('renU@17')
    pwd=hashlib.md5(pwd.encode('utf-8')).hexdigest()
    print(uname, pwd)
    u=Customer.objects.filter(username=uname,pwd=pwd)
    if(u):
        response=render(request,'l.html')
        response.set_cookie('username',uname)
        return response
    else:
            return render(request,'login.html')
        
def msearch(request):
    coursename=request.GET.get('coursename')
    course_list=course.objects.filter(course_name__icontains=coursename) 
    str= '''
    <h2>Matched Collections</h2>
    <table class="w3-table-all"style="width:60%";>
    <thread>
    <tr class="w3-red">
    <th>course Name</th>
    <th>courseid</th>
     
    </tr>
    </thread>
    '''
    # for course in course_list:
    # str+="<tr><td>"+.course_name+"</td><td>"+course.hero="<td><td>"+course.heroine+"
    # </td></tr>";

# return HttpResponse(str)



    



