from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

#Create your forms here
class LoginForm(AuthenticationForm):
    username = forms.CharField(
    	widget = TextInput(
    		attrs={
    			'class':'form-control',
    			'placeholder': 'Usuário'
    		}
    	)
    )
    password = forms.CharField(
    	widget = PasswordInput(
    		attrs={
    			'class':'form-control',
    			'placeholder': '*******'
    		}
    	)
    )

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Usuário',
                }
            ),
            'first_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Sobrenome',
                }
            ),
            'email': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'E-mail',
                }
            ),
            'password1': PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Senha',
                }
            ),
            'password2': PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirmar senha',
                }
            ),
        }