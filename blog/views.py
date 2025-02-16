from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('Página Blog acessada')
    return render(
        request,
        'blog/index.html'
    )

def postagens(request):
    print('Página de postagens do Blog acessada')
    return render(
        request,
        'blog/postagens.html'
    )