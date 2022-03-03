from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)[0]  #fetching the first using like [0] or .first()
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)
    # return HttpResponse(f"I am in blogPost : {slug}")