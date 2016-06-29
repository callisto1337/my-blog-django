from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post

def post_list(request):
	posts = Post.objects.all()[:5]
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

def auth(request):
	if request.user.is_authenticated():
		return redirect('/')
	elif request.method == 'POST':
		form_auth = AuthenticationForm(request=request, data=request.POST)
		form_auth.fields['username'].widget.attrs.update({'placeholder': 'Username'})
		form_auth.fields['password'].widget.attrs.update({'placeholder': 'Password'})
		if form_auth.is_valid():
			user = form_auth.get_user()
			login(request, user)
			return redirect("/")
	else:
		form_auth = AuthenticationForm()
		form_auth.fields['username'].widget.attrs.update({'placeholder': 'Username'})
		form_auth.fields['password'].widget.attrs.update({'placeholder': 'Password'})
	return render(request, "blog/auth.html", {'form_auth': form_auth})

def reg(request):
	if request.user.is_authenticated():
		return redirect('/')
	elif request.method == 'POST':
		form_reg = UserCreationForm(request.POST)
		form_reg.fields['username'].widget.attrs.update({'placeholder': 'Username'})
		form_reg.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
		form_reg.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
		if form_reg.is_valid():
			new_user = form_reg.save()
			return redirect('/auth/')
	else:
		form_reg = UserCreationForm()
		form_reg.fields['username'].widget.attrs.update({'placeholder': 'Username'})
		form_reg.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
		form_reg.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
	return render(request, "blog/reg.html", {'form_reg': form_reg})

def logout_view(request):
	logout(request)
	return redirect('/')
