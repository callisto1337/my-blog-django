from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
	posts = Post.objects.all()[:5]
	return render(request, 'blog/post_list.html', {'posts': posts})

def sign_up(request):
	return render(request, 'blog/sign_up.html')