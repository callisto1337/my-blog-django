from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .models import Post
from .forms import FormAuth


def post_list(request):
	posts = Post.objects.all()[:5]
	return render(request, 'blog/post_list.html', {'posts': posts})

def auth(request):
	form_auth = FormAuth()

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			return HttpResponse("Success.")
		else:
			return HttpResponse("Error.")
	else:
		return render(request, 'blog/auth.html', {'form_auth': form_auth})
