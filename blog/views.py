from django.shortcuts import render,redirect
from blog.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth 

# Create your views here.
def home(request):
  if request.method == 'POST':
    title = request.POST.get('title','')
    content = request.POST.get('content','')
    id1 = request.POST.get('id1','')
    blog = Blog()
    blog.title = title
    blog.content = content
    blog.id1 = id1
    blog.save()
    bloglist = Blog.objects.all()
    return render(request,'home.html',{'bloglist':bloglist})
  elif request.method == 'GET':
    bloglist = Blog.objects.all()
    return render(request,'home.html',{'bloglist':bloglist})
def login(request):
  if request.method == 'GET':
    return render(request,'login.html')
  elif request.method == 'POST':
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    if user is not None and user.is_active:
      auth.login(request,user)
      return redirect('/home')
    else:
      return render(request,'login.html')
def register(request):
  if request.method == 'GET':
    return render(request,'register.html')
  elif request.method == 'POST':
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = User.objects.create_user(username,'',password)
    user.is_staff = False
    user.save()
    print request.user
    return render(request,'login.html')

