from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserLogin
# Create your views here.

def home(request):
    return render(request, 'crud/home.html')

def addinfo(request):
    if request.method == "POST":

        fm = UserLogin(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ag = fm.cleaned_data['age']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,age=ag,password=pw)
            reg.save()
            fm = UserLogin()
            return render(request, 'crud/home.html')
    else:
        fm = UserLogin()
    return render(request, 'crud/signup.html',{'form':fm})

def login(request):
    return render(request, 'crud/login.html')

def loginrecord(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        pi = User.objects.get(email=email)
        if pi.email == email and pi.password == password:
            return render(request, 'crud/dashboard.html',{'form':pi})
    return render(request, 'crud/login.html')


def delete(request,id):
    if request.method == "POST":
        pi = User.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update(request, id):
    if request.method == "POST":
        pi = User.objects.get(id=id)
        fm = UserLogin(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(id=id)
        fm = UserLogin(instance=pi)
        return render(request, 'crud/updateuser.html',{'form':fm})
    
def showdata(request):
        stud = User.objects.all()
        return render(request, 'crud/showdata.html', {'stu':stud})
