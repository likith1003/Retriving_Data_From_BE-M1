from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        cls = request.POST.get('cls')
        un = request.POST.get('un')
        pw = request.POST.get('pw')

        student = Student(sname=name, spno=pno, email=email, username=un, pw=pw, cls=cls)
        student.save()
        return HttpResponse('registeration is successfull')
    return render(request, 'register.html')


def users(request):
    users = Student.objects.all()
    d = {'users': users}
    return render(request, 'users.html', d)