from django.http import HttpResponse
from django.shortcuts import render, redirect
from audioop import reverse
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    return render(request, 'women/index.html')

def about(request):
    return render(request, 'women/about.html')

def russian(request):
    return render(request, 'women/russian.html')

def ussr(request):
    return render(request, 'women/ussr.html')

def gaming(request):
    return render(request, 'women/gaming.html')

def persona(request):
    return render(request, 'women/persona.html')


def persona(request):
    return HttpResponse(' <h1> Привет это мои сайты выбирай любой и заходи !!! <br> Про игры: <a href="http://127.0.0.1:8000/gaming/">Gaming</a>". <br> Про Росссию:  <a href="http://127.0.0.1:8000/russian/">russian</a>". <br> Про СССР:  <a href="http://127.0.0.1:8000/ussr/">ussr</a>". </h1> ')

def categories(request, cat_id, uri=None):
        if cat_id > 2020:
            urli = reverse('home')
            return redirect(uri)
        return HttpResponse(f'Это номер {cat_id}')