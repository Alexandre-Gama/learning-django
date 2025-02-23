from django.shortcuts import render
from django.http import HttpRequest
from blog.data import posts
from typing import Any

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
def post(request: HttpRequest, post_id: int):
    print('Post', post_id)

    found_post: dict[str, Any] | None = None
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Exception('Post não existe.')

    context={
            'posts': [found_post],
            'title': found_post['title'] + ' - '
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