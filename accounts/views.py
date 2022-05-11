from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import UserModels
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods

# Create your views here.
@require_GET
def signup(request):
    return render(request, 'accounts/signup.html', {})

@require_POST
def createUser(request):
    try:
        exist_email = User.objects.get(email=request.POST['field-email'])
        exist_username = User.objects.get(username=request.POST['field-username'])
        if exist_email or exist_username:
            return render(request, 'accounts/signup.html', { 'error' : 'Usuário já existe'})
    except User.DoesNotExist:
        new_username = request.POST['field-username']
        new_email = request.POST['field-email']
        new_password = request.POST['field-password']

        new_account = User.objects.create(username=new_username, email=new_email, password=new_password)
        new_account.save()

        new_user = UserModels.objects.create(name=new_account)
        new_user.save()

    return HttpResponseRedirect('/feed/')  

@require_http_methods(["GET", "POST"])
def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['field-username']
            password = request.POST['field-password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/feed/')  
            return render(request, 'posts/home.html', {'error' : 'Usuário ou senha incorreto'})
        elif request.method == 'GET':
            return render(request, 'accounts/login.html')
    else:
        return HttpResponseRedirect('/feed/')    

@login_required
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('')

# update without password
@require_http_methods(["GET", "POST"])
def updateUser(request, name=None):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if request.method == 'POST':
            if user is None:
                render(request, 'accounts/update-user.html', {'error': 'Atualização não concluída. Tente novamente mais tarde'})
            else:
                user.username = request.POST['field-username']
                user.email = request.POST['field-email']
                user.save()

                return render(request, 'posts/home.html', {'update': 'Dados atualizados com sucesso'})

        elif request.method == 'GET':
            username = user.name
            email = user.name
            context = {
                'username' : username,
                'email' : email,
            }
            return render(request, 'accounts/update-user.html', context)