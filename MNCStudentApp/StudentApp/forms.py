from django import forms

class LoginForm(forms.Form):
    user_id = forms.CharField(label='User ID', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)