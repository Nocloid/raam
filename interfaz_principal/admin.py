from django.contrib import admin
from .models import contacto, Post

# registering the model
class contactos_mostrar(admin.ModelAdmin):
    search_fields = ["nombre"]
    list_display = ["nombre", "correo", "telefono", "asunto", "mensaje"]

admin.site.register(contacto, contactos_mostrar)
admin.site.register(Post)