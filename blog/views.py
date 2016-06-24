from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post

def post_list(request):
	posts = Post.objects.all()[:5]
	return render(request, 'blog/post_list.html', {'posts': posts})

def auth(request):
    if request.user.is_authenticated():
        return redirect('/')
    elif request.method == 'POST':
        form_auth = AuthenticationForm(request=request, data=request.POST)
        if form_auth.is_valid():
            user = form_auth.get_user()
            login(request, user)
            return redirect("/")
    else:
        form_auth = AuthenticationForm()
    return render(request, "blog/auth.html", {'form_auth': form_auth})

def reg(request):
	if request.user.is_authenticated():
		return redirect('/')
	elif request.method == 'POST':
		form_reg = UserCreationForm(request.POST)
		if form_reg.is_valid():
			new_user = form_reg.save()
			return redirect('/auth/')
	else:
		form_reg = UserCreationForm()
	return render(request, "blog/reg.html", {'form_reg': form_reg})

def logout_view(request):
	logout(request)
	return redirect('/')
