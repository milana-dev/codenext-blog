from django.shortcuts import render
from django.http import  HttpResponse

from blogs.models import Blog
from blogs.forms import BlogFrom
# Create your views here. 

def all_blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'all_blogs.html', context)




