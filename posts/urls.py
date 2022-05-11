from django.urls import path
from posts.views import createPost

app_name = 'account' 

urlpatterns = [
    path('post/create/', createPost, name='create'),
    # path('feed/', , name='signup'),
    # path('create-user/', createUser, name='create'),
    # path('logout/', logoutUser, name='logout'),
    # path('update-user/', updateUser, name='update'),
]
