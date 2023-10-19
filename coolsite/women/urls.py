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

    path('cats/<int:cat_id>/', categories, name='spisok'),
}




   # path('megagidon/', megagidon),




   # path('gaming/', gaming),
  #  path('personality/', personality),
  #  path('slavaSSSR/', slavaSSSR),
  #  path('russian/', views.categories, name='spisok'),
#}