from django.shortcuts import render

# Create your views here.
def index(request):
    print('Home acessada')

    context={
            'text': 'Estamos na home'
        }
    
    return render(
        request,
        'home/index.html',
        context
    )