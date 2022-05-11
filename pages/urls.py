from django.urls import path
from pages.views import landingPage

app_name = 'account' 

urlpatterns = [
    path('', landingPage, name='home'),
]