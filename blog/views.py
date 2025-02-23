from django.shortcuts import render
from blog.data import posts

# Create your views here.
def index(request):
    print('Página Blog acessada')

    context={
            'text': 'Estamos no Blog',
            'title': 'Página do Blog - ',
            'posts': posts
        }
    
    return render(
        request,
        'blog/index.html',
        context
    )

# Create your views here.
def post(request, id):
    print('Post', id)

    context={
            'posts': posts
        }
    
    return render(
        request,
        'blog/index.html',
        context
    )

def postagens(request):
    print('Página de postagens do Blog acessada')

    context={
            'text': 'Estamos em postagens',
            'title': 'Página de Postagens - '
        }
    
    return render(
        request,
        'blog/postagens.html',
        context
    )