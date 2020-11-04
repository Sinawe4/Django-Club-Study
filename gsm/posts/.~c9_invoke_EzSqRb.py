from django.shortcuts import render

from .models import Post
# Create your views here.
from django.http import HttpResponse

def index(request):
   posts = Post.objects.all()
   context = {'posts' : posts}
   
   return render (request, 'posts/index.html', context)
