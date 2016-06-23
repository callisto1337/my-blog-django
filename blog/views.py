from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .models import Post
from .forms import FormAuth, FormReg


def post_list(request):
	posts = Post.objects.all()[:5]
	return render(request, 'blog/post_list.html', {'posts': posts})

def auth(request):
	if request.user.is_authenticated():
		return redirect('/')
	if request.method == 'POST':
		form_auth = FormAuth(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			return render(request, 'blog/auth.html', {'form_auth': form_auth})
	else:
		form_auth = FormAuth()
	return render(request, 'blog/auth.html', {'form_auth': form_auth})

def reg(request):
	form_reg = FormReg()
	if request.user.is_authenticated():
		return redirect('/')
	return render(request, 'blog/reg.html', {'form_reg': form_reg})

def logout_view(request):
	logout(request)
	return redirect('/')
