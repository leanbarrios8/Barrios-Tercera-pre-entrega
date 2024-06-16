from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from bitcoin.forms import CrearMoneda
from bitcoin.models import Moneda

def bitcoin(request):
    return render(request, 'blexo\index.html')

def lista(request):
    monedas = Moneda.objects.all()
    return render(request, 'blexo/lista.html', {'monedas': monedas})

def monedas(request):
    print('Valor de la request: ', request)
    print('Valor de GET: ', request.GET)
    print('Valor de POST: ', request.POST)

    if request.method == 'POST':
        formulario = CrearMoneda(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista')

    else:
        formulario = CrearMoneda()

    monedas = Moneda.objects.all()
    return render(request, 'blexo/monedas.html', {'formulario': formulario, 'monedas': monedas})

