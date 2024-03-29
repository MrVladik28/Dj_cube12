from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from audioop import reverse
from django.template.loader import render_to_string

# Create your views here.
from .models import Women, Book_Love

menu = [{'title': 'Главная страница', 'url_n': 'home'},
        {'title': 'kapibara', 'url_n': 'kapibara'},
        {'title': 'it_cube32', 'url_n': 'it_cube/32'},
        {'title': 'russian', 'url_n': 'russian'},



        ]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]




def index(request):
    women = Women.objects.filter(is_published=1)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'women': women,
    }
    return render(request, 'women/index.html', context=data)




kapibara1 = [
    "https://yt3.googleusercontent.com/vgi0TjoJrQhch_15n8xGsX-8R-y9RpU3kBaOSOpZq8xYoiq496DpcHNVbjmLZQOJps5WdswKvQ=s900-c-k-c0x00ffffff-no-rj",
    "https://phonoteka.org/uploads/posts/2023-04/1680366535_phonoteka-org-p-tank-kapibara-art-vkontakte-6.jpg",
    "https://mykaleidoscope.ru/uploads/posts/2023-05/1685063826_mykaleidoscope-ru-p-kapibara-s-manikyurom-krasivo-17.jpg",
    "https://phonoteka.org/uploads/posts/2023-04/1680702574_phonoteka-org-p-kapibara-estetika-art-vkontakte-45.jpg",
    "https://steamuserimages-a.akamaihd.net/ugc/2005845300450558809/D5B7CBC12DE256998A4F2342B9FC96C494A0A548/?imw=512&amp;imh=512&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true",
    "https://phonoteka.org/uploads/posts/2023-03/1679708784_phonoteka-org-p-mertvaya-kapibara-oboi-vkontakte-44.jpg",
    "https://sun9-53.userapi.com/impg/XQ8_Q-9qU8is2yWTR9fEigqsmEH60wDOEejHjg/pBrXL0X0SxI.jpg?size=604x604&quality=96&sign=43fc16c1144c3fa6bb63ea4ba4f5dd79&c_uniq_tag=pNVC6KWZ5QiYOF1QXSXiUVHltC4IjTyEeoFCCnGpdU0&type=album",
    "https://sun6-20.userapi.com/s/v1/ig2/xSQvkHdpQCyUNdFT-F-eiD-J3i5UFNxJYPO_Zf3ZsdxBUleOZ2avE2KJa7x2WkW0AvDEv_ND5_wu5GqW2c7evCPg.jpg?size=1080x1080&quality=95&crop=38,0,1080,1080&ava=1",
    "https://damion.club/uploads/posts/2022-01/1642903638_15-damion-club-p-kapibara-smeshnaya-15.jpg",
    "https://mykaleidoscope.ru/uploads/posts/2023-05/1685063912_mykaleidoscope-ru-p-kapibara-s-manikyurom-krasivo-40.jpg",
    ]


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})

def spisok(request):
    data = {

        'menu': menu,
    }
    return render(request, 'women/spisok.html')




def russian(request):
    return render(request, 'women/russian.html')


def kapibara(request):
    data = {
        'kapibara1': kapibara1,
    }
    return render(request, 'women/kapibara.html', data)


def how_women(request, women_id):
    women = get_object_or_404(Women, pk=women_id)
    data = {
        'title': women.titile,
        'menu': menu,
        'women': women,
        'cat_selected': 1,



    }
    return render(request, 'women/women.html', data)


def how_book(request, book_slug):
    book = get_object_or_404(Book_Love, slug=book_slug)
    data = {
        'title': 'это страница книги',
        'menu': menu,
        'book': book,
        'cat_selected': 1,



    }

    return render(request, 'women/book.html', data)


def ussr(request):
    return render(request, 'women/ussr.html', context={'menu': menu})


def gaming(request):
    return render(request, 'women/gaming.html')


def persona(request):
    return render(request, 'women/persona.html')


def it_cube32(request):
    return render(request, 'women/it_cube32.html.html')


def categories(request, cat_id, uri=None):
    if cat_id > 2020:
        urli = reverse('home')
        return redirect(uri)
    return HttpResponse(f'Это номер {cat_id}')
