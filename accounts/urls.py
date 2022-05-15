from django.urls import path
from accounts.views import signup, loginUser, logoutUser, updateUser, validateUsername

app_name = 'account' 

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('signup/', signup, name='signup'),
    path('validate-username/', validateUsername, name='validate'),
    path('logout/', logoutUser, name='logout'),
    path('update-user/', updateUser, name='update'),
]
