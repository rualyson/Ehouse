# Autenticação Django

![layout](https://i.imgur.com/BVMz7tL.png)

Essa aplicação pode ser usada em qualquer projeto, a mesma consite em duas funcionalidades

* Login
* Criação de novo usuário
* Logout (não há uma tela fisica, somente o 'method logout')

## Front-end

O layout foi montado com base no Bootstrap v4

## Getting Started

Inicialmente você deve clonar este repositório dentro do seu projeto Django

Feito isso, você deve incluir o app dentro do seu arquivo _setings.py_ 

```
INSTALLED_APPS = [
    ...
    'accounts',
    ...
]
```

## Include url

Dentro do arquivo `urls.py` é necessário incluir a url do accounts:

```
urlpatterns = [
    ...
    path('admin/', admin.site.urls),
    
    # accounts include
    path('accounts/', include('accounts.urls')),
    ...
]
```

## Configurando redirecionamento de login

Após realizar o login, o usuário deve ser redirecionado para uma tela de acesso, normalmente a home page do sistema

Sendo assim, dentro do arquivo _setings.py_ adicione os seguintes campos no final do arquivo

```
...
LOGIN_URL = '/accounts/login' # Não altere essa linha
LOGIN_REDIRECT_URL = '/' # Caminho para a home da aplicação
...
```

## Migrations

Execute a migration para sincronizar o banco de dados e criar todos os campos utilizados

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```
## URLs de acesso
* Login: http://localhost:8080/accounts/login
* cadas: http://localhost:8080/accounts/cadastro
* Logout: http://localhost:8080/accounts/logout

## Restrição de acesso

Após o usuário estar logado, não é mais possível acessar as telas de login ou de registro. Isto está configurado via javascript no próṕrio template da seguinte forma:

### _accounts/templates/core/login.html_ 

```
{% if user.is_authenticated %}
	<script>
		setTimeout(function(){window.location.href="/"},0.0);
	</script>  
{% else %}
```

O código acima é um javascript dentro do arquivo _login.html_
Se essa página for acessada com o usuário logado, ele será redirecionado para a home page da aplicação "/"
