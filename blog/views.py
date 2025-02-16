from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('Página Blog acessada')
    return HttpResponse('Você está na página Blog...')

def postagens(request):
    print('Página de postagens do Blog acessada')
    return HttpResponse('Você está na página de postagens do Blog...')