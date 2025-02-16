from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('Home acessada')
    return HttpResponse('Você está na Home do Site...')