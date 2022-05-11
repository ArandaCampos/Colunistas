from django.shortcuts import render
from accounts.models import PostsModels, UserModels
from django.views.decorators.http import require_GET, require_safe
from django.contrib.auth.models import User

# Create your views here.
@require_safe
def createPost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                account = User.objects.get(username__exact=request.user.username)
                try:
                    user = UserModels.objects.get(name__exact=account)
                except:
                    return render(request, 'posts/create-post.html', {'error': 'Falha de conexão com o servidor. Tente novamente mais tarde'})
            except:
                return render(request, 'posts/create-post.html', {'error': 'Falha de conexão com o servidor. Tente novamente mais tarde'})
            
            title_user = request.POST['field-title']
            text_user = request.POST['field-text']
            posts = PostsModels.objects.create(author=user, title=title_user, text=text_user, like=0)
            posts.save()
            
            return render(request, 'posts/home.html', {'msg': 'Publicação concluída'})
        elif request.method == "GET":
            return render(request, 'posts/create-post.html')
            
@require_GET
def listPost(request):
    if request.user.is_authenticated:
        try:
            account = User.objects.get(username__exact=request.user.username)
            try:
                user = UserModels.objects.get(name__exact=account)
                following = user.following
                return render(request, 'feed.html')
            except:
                return render(request, 'feed.html', {'error': 'Erro de autenticação'})
        except:
            return render(request, 'feed.html', {'error': 'Erro de autenticação'})