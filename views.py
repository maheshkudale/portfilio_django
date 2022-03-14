from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobno=request.POST['mobno']
        message=request.POST['message']
        if name!="None" and email!="None" and mobno!="None" and message!="None":
            obj=Contact(name=name,email=email,mobno=mobno,message=message)
            obj.save()
    return render(request,'contact.html')

def project(request):
    return render(request,'project.html')

