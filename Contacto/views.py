from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    form_contacto = FormularioContacto()
    return render(request, 'Contacto/contacto.html', {'miFormulario':form_contacto})
