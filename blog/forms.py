from django import forms

class ContactForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	
	subject = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'placeholder': 'Тема сообщения', 'class': 'form-control'}))
	sender = forms.EmailField(widget = forms.EmailInput(attrs = {'placeholder': 'Ваш Email', 'class': 'form-control'}))
	message = forms.CharField(widget = forms.Textarea(attrs = {'placeholder': 'Текст сообщения', 'class': 'form-control'}))


