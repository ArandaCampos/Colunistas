from django.urls import path
from posts.views import createPost, listPost, profile, detailPost

app_name = 'account' 

urlpatterns = [
    path('post/create/', createPost, name='create'),
    path('home/', listPost, name='feed'),
    path('profile/', listPost, name='profile'),
    path('post/<slug:slug>/', detailPost, name='detailpost'),
    path('home/profile', profile, name='myprofile'),
    path('author/<str:accounts>/', listPost, name='detailpost'),
    # path('create-user/', createUser, name='create'),
    # path('logout/', logoutUser, name='logout'),
    # path('update-user/', updateUser, name='update'),
]
