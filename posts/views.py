from django.http import HttpResponse
from django.shortcuts import render
from accounts.models import PostsModels, UserModels
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.models import User

# Create your views here.
@require_http_methods(['GET', 'POST'])
def createPost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                user = UserModels.objects.get(name__exact=request.user.username)
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
def listPost(request, accounts=None):
    if request.user.is_authenticated:
        try:
            if accounts == None:
                people = UserModels.objects.get(name__username__exact=request.user.username).following.filter()
                accounts_list = list(people)
                posts = PostsModels.objects.filter(author__name__username__in=accounts_list)
            else:
                posts = PostsModels.objects.filter(author__name__username__exact=accounts)
        except:
            return render(request, 'posts/home.html', {'posts': 'Erro de autenticação'})
        context = {
            'posts' : posts
        }
        return render(request, 'posts/home.html', context)

@require_GET
def detailPost(request, slug):
    if request.user.is_authenticated:
        try:
            posts = PostsModels.objects.filter(slug__exact=slug)
        except:
            return render(request, 'posts/home.html', {'posts': 'Falha na conexão com o servidor'})
        context = {
            'posts' : posts
        }
        return render(request, 'posts/home.html', context)

@require_POST
def add_following(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                following = UserModels.objects.get(id__exact=id)
                user = User.objects.get(username__exact=request.user.username)
                userModels = UserModels.objects.get(name__username__exact=user)
                try:
                    userModels.folowing.add(following)
                except:
                    pass
            except:
                pass

@require_GET
def profile(request):
    if request.user.is_authenticated:
        posts = PostsModels.objects.filter(author__name__username__exact=request.user.username)
        context = { 'posts' : posts}
        return render(request, 'posts/profile.html', context)
    else:
        return render(request, 'accounts/login.html')