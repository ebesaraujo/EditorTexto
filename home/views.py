from .models import Artigo
from django.http import HttpResponse
from django.shortcuts import render
import json

def home(request):
    artigos = Artigo.objects.all()
    return render(request, 'home.html', {'artigos': artigos})

def salvar(request):
    dados = json.loads(request.body)
    artigo = Artigo(conteudo_artigo=dados['artigo'])
    artigo.save()
    return HttpResponse("1")