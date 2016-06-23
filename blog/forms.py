from django import forms
# from django.contrib.auth import login


class FormAuth(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)

class FormReg(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)
    conf_password = forms.CharField(label='Confirm password', max_length=30, widget=forms.PasswordInput)