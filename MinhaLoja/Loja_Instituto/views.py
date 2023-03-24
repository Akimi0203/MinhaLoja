from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Clientes
import requests


from pyexpat.errors import messages


# Create your views here.
def cadastro(request):
    return HttpResponse("Stay calm and be Happy!")

def acesso(request):
    return HttpResponse("Aqui será desenvolvido o acesso ao sistema")

def raiz(request):
     #return render(requests,'home.html')
     cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
     cotacao = cotacao.json()
     cotacao_dolar = cotacao["USDBRL"]["bid"]
     timestamp_dolar = cotacao["USDBRL"]["create_date"]

     return render(request, 'home.html',{'cotacao_dolar':cotacao_dolar, 'horario': timestamp_dolar})

def cliente(request):
    return render(request,'cliente.html')


def produto(request):
    return render(request,'produto.html')



def salvar(request):
    lista = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN", "RS", "RO","RR","SC","SP","SE", "TO"]
    nome = request.POST.get("Nome")
    cpf = request.POST.get("CPF")
    endereco = request.POST.get("Endereco")
    cidade = request.POST.get("Cidade")
    estado = request.POST.get("Estado")

    if nome == "" or cpf == "" or endereco == "" or cidade == "" or estado == "":
        messages.info(request, "Alguma das informações é inválida")
        return redirect("MinhaLoja/cliente")

    else:
        if estado not in lista:
            messages.info(request,"Coloque uma sigila Válida!")
            return redirect("MinhaLoja/cadastro")
        elif Clientes.objects.filter(CPF=cpf).exists():
            messages.info(request,"CPF já cadastrado!")
            return redirect("MinhaLoja/cliente")
        else:
            ok = Clientes(
                Nome=nome,
                CPF=cpf,
                Endereco=endereco,
                Cidade=cidade,
                Estado=estado,
            )
            ok.save()
            return render(request,"cliente.html",{"nome": nome, "cpf": cpf, "endereco": endereco, "cidade": cidade, "estado": estado})






