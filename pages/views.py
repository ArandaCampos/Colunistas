from django.shortcuts import render
from django.views.decorators.http import require_GET

# Create your views here.
@require_GET
def landingPage(request):
    return render(request, 'landing-page.html')