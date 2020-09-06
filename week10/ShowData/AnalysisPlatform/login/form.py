from django import forms

class regForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    conform_password = forms.CharField(widget=forms.PasswordInput, min_length=8)

class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)