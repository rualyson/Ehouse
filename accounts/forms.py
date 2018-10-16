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

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')
    def __init__ (self, *args, **kwargs):
        super (RegisterForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['username'].widget.attrs['placeholder'] = 'Nome do usuário'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['password1'].widget.attrs['placeholder'] = 'Digite sua senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme sua senha'
        
    def save (self, commit = True):

        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user 

	# verifica se tem possui o email
    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe um usuário com esse e-mail')
        return email
        
class EditAccountsForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email = email).exclude(pk = self.instance.pk)
        if(queryset.exists()):
            raise forms.ValidationError('Já existe usuário com este email')
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']