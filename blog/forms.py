from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# class FormAuth(forms.Form):
#     username = forms.CharField(label='Username', max_length=30, required=True)
#     password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)

# class FormReg(FormView):
#     form_class = UserCreationForm

#     success_url = "/auth/"
#     template_name = "blog/reg.html"

#     def form_valid(self, form):
#         form.save()
#         return super(RegisterFormView, self).form_valid(form)

# class FormReg(forms.Form):
#     username = forms.CharField(label='Username', max_length=30, min_length=6, required=True)
#     email = forms.EmailField(label='Email', max_length=50, min_length=6)
#     password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput, min_length=6)
#     conf_password = forms.CharField(label='Confirm password', max_length=30, widget=forms.PasswordInput, min_length=6)

#     def validate(self, value):
#     	data = self.cleaned_data['recipients']
#     	if password != conf_password:
#     		raise forms.ValidationError("You have forgotten about Fred!")
#     	return data