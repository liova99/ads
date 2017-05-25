from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)  #  specify that, that is a password field


    #  information about your class
    class Meta:
        model = User
        fields = ['username', 'email', 'password']