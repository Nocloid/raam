from django.shortcuts import render
from .models import contacto, Post
from .forms import contacto_form

# Create your views here.
def Inicio(request):
    return render(request, 'interfaz_principal/Inicio.html')


def Nosotros(request):
    return render(request,'interfaz_principal/nosotros.html')

def Proyectos(request):
    return render(request,'interfaz_principal/proyectos.html')
    
def Galeria(request):
    posts = Post.objects.all()
    return render(request,'interfaz_principal/Galerias.html', {"posts": posts})

def Contactos(request):
    data = {
        'form':contacto_form
    }
    if request.method == 'POST':
        formulario = contacto_form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data['form'] = formulario
    return render(request,'interfaz_principal/contactos.html', data)

def posts(request, id):
    posts = Post.objects.get(id=id)
    return render(request, 'interfaz_principal/posts.html', {"posts": posts})
