from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.

def home(req):
    blogs = Blog.objects
    return render(req, 'home.html', {'blogs': blogs})

def detail(req,blog_id): 
    details = get_object_or_404(Blog, pk= blog_id)
    return render(req, 'detail.html', {'details': details})

def new(req):  #new.html을 띄워주는 함수
    return render(req, 'new.html')

def create(req):  #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = req.GET['title']
    blog.body = req.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
