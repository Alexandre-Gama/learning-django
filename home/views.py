from django.shortcuts import render

# Create your views here.
def index(request):
    print('Home acessada')
    return render(
        request,
        'home/index.html'
    )