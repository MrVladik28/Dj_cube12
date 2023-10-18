from django.http import HttpResponse
from django.shortcuts import render, redirect
from audioop import reverse
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    #t = render_to_string('women/index.html')
   #return HttpResponse(t)
    return render(request, 'women/index.html')

def about(request):
    return render(request, 'women/about.html')

def megagidon(request):
    return HttpResponse('чундра чучундра  <br>  шакатака <br> ЛЯЛЯ  ПИПИ ')

def gaming(request):
    return HttpResponse(' <img height="50%" src= "https://pic.rutubelist.ru/video/65/65/6565133a32baee8c35c92699844e6e4c.jpg" \> <h1> чундра чучундра  <br> бум бум шакатака <br> ЛЯЛЯ  ПИПИ </h1> ')

def personality(request):
    return HttpResponse(' <img height="50%" \> <h1> чундра чучундра  <br> бум бум шакатака <br> ЛЯЛЯ  ПИПИ </h1> ')

def slavaSSSR(request):
    return HttpResponse(' <img height="50%" src= "https://m.politnavigator.net/wp-content/uploads/2021/05/scale_1200-6.jpg" \>  <h1> СЛАВА СОВЕТСКОМУ СОЮЗУ  <br> СЛАВА СОВЕТСКОМУ СОЮЗУ <br> ЗА РОДИНУ ЗА СТАЛИНА </h1> ')

def russion(request):
    return HttpResponse(' <img height="50%" src= "https://sopranoclub.ru/images/kartinki-flag-rossii/file40156.jpg" \> <h1> СЛАВА РОССИИ <br> РОССИЯ СВЕЩЕННАЯ НАША СТРАНА <br> СЛАВА ПУТИНУ СЛАВА РОССИИ  </h1>  ')

def categories(request, cat_id, uri=None):
        if cat_id > 2020:
            urli = reverse('home')
            return redirect(uri)
        return HttpResponse(f'Это номер {cat_id}')