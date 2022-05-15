from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import UserModels
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods

# Create your views here.
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html', {})
    elif request.method == 'POST':
        try:
            exist_user = User.objects.filter(email__exact=request.POST['field-email']).exists()
            exist_email = User.objects.filter(username__exact=request.POST['field-username']).exists()
        except User.DoesNotExist:
            pass
        if (exist_user or exist_email):
            return JsonResponse({ 'msg' : 'Usuario ou Email ja existe'}, status=500)

        new_username = request.POST['field-username']
        new_email = request.POST['field-email']
        new_password = request.POST['field-password']

        new_account = User.objects.create(username=new_username, email=new_email, password=new_password)
        new_account.save()

        new_user = UserModels.objects.create(name=new_account)
        new_user.save()

        return HttpResponseRedirect('/home/')

def validateUsername(request):
    username = request.GET.get('field-username', None)
    email = request.GET.get('field-email', None)
    response = {
        'exist_user': User.objects.filter(username__iexact=username).exists(),
        'exist_email': User.objects.filter(email__iexact=email).exists(),
    }
    return JsonResponse(response)

@require_http_methods(["GET", "POST"])
def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username_input = request.POST['field-username']
            password_input = request.POST['field-password']
            user = User.objects.filter(username__exact=username_input)
            username_data = user.first().username
            pass_data = user.first().password
            if (username_input == username_data and password_input == pass_data):
            # user = authenticate(username=username_input, password=password_input)
            # if user is not None:
                user = User.objects.get(username__exact=username_input)
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return JsonResponse({'error' : 'Usuário ou senha incorreto'}, status=406)
        elif request.method == 'GET':
            return render(request, 'accounts/login.html')
    else:
        return HttpResponseRedirect('/home/')

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