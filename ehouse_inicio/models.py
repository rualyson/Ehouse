from django.db import models
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.models import User


class Usuario(AuthenticationForm):
    username = forms.CharField(label="Usuário", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Senha", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
    
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','email','password']
    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


