from django.urls import path

from women import views
from women.views import *



urlpatterns = {
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('russian/', views.russian, name='russian'),
    path('ussr/', views.ussr, name='ussr'),
    path('gaming/', views.gaming, name='gaming'),
    path('persona/', views.persona, name='persona'),
    path('it_cube/32', views.it_cube32, name='it_cube32'),
    path('kapibara', views.kapibara, name='kapibara'),
    path('cats/<int:cat_id>/', categories, name='spisok'),
    path('women_id/<int:women_id>/', views.how_women, name='women'),
    path('book_id/<int:book_id>/', views.how_book, name='book'),
}




   # path('megagidon/', megagidon),




   # path('gaming/', gaming),
  #  path('personality/', personality),
  #  path('slavaSSSR/', slavaSSSR),
  #  path('russian/', views.categories, name='spisok'),
#}