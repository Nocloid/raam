from django.urls import path
from . import views


urlpatterns = [
    path('',views.Inicio, name='Inicio'),
    path('nosotros',views.Nosotros , name='Nosotros'),
    path('proyecto',views.Proyectos , name='Proyectos'),
    path('galeria',views.Galeria , name='Galeria'),
    path('contactos',views.Contactos , name='Contactos'),
    path('post/<int:id>', views.posts, name="posts"),
]