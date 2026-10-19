from django import forms

class LoginForm(forms.Form):
    usern_id = forms.CharField( widget=forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'User Id'

                }))
    password = forms.CharField( widget=forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Password'

                }))