from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

def post_list(request):
	posts = Post.objects.all()[:5]
	return render(request, 'blog/post_list.html', {'posts': posts})

def about(request):
	return render(request, 'blog/about.html')

def contacts(request):
	if request.method == 'POST':
		form_contact = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form_contact.is_valid():
			subject = form_contact.cleaned_data['subject']
			sender = form_contact.cleaned_data['sender']
			message = form_contact.cleaned_data['message']

			recipients = ['live_forecast@mail.ru']
			try:
				send_mail(subject, message, 'hazardous333@gmail.com', recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'blog/contacts.html')
	else:
		#Заполняем форму
		form_contact = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'blog/contacts.html', {'form_contact': form_contact})


def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

def auth(request):
	if request.user.is_authenticated():
		return redirect('/')
	elif request.method == 'POST':
		form_auth = AuthenticationForm(request=request, data=request.POST)
		form_auth.fields['username'].widget.attrs.update({'placeholder': 'Имя пользователя'})
		form_auth.fields['password'].widget.attrs.update({'placeholder': 'Пароль'})
		if form_auth.is_valid():
			user = form_auth.get_user()
			login(request, user)
			return redirect("/")
	else:
		form_auth = AuthenticationForm()
		form_auth.fields['username'].widget.attrs.update({'placeholder': 'Имя пользователя'})
		form_auth.fields['password'].widget.attrs.update({'placeholder': 'Пароль'})
	return render(request, "blog/auth.html", {'form_auth': form_auth})

def reg(request):
	if request.user.is_authenticated():
		return redirect('/')
	elif request.method == 'POST':
		form_reg = UserCreationForm(request.POST)
		form_reg.fields['username'].widget.attrs.update({'placeholder': 'Имя пользователя'})
		form_reg.fields['password1'].widget.attrs.update({'placeholder': 'Пароль'})
		form_reg.fields['password2'].widget.attrs.update({'placeholder': 'Подтверждение пароля'})
		if form_reg.is_valid():
			new_user = form_reg.save()
			return redirect('/auth/')
	else:
		form_reg = UserCreationForm()
		form_reg.fields['username'].widget.attrs.update({'placeholder': 'Имя пользователя'})
		form_reg.fields['password1'].widget.attrs.update({'placeholder': 'Пароль'})
		form_reg.fields['password2'].widget.attrs.update({'placeholder': 'Подтверждение пароля'})
	return render(request, "blog/reg.html", {'form_reg': form_reg})

def logout_view(request):
	logout(request)
	return redirect('/')
