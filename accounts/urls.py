from django.urls import path
from accounts.views import signup, createUser, loginUser, logoutUser, updateUser

app_name = 'account' 

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('signup/', signup, name='signup'),
    path('create-user/', createUser, name='create'),
    path('logout/', logoutUser, name='logout'),
    path('update-user/', updateUser, name='update'),
]
