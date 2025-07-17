from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadoras(request):
    jogadoras = [
        {"Nome": "Lorena", "Idade": "28 anos", "Posicao": "Goleira", "Naturalidade": "Ituverava - SP", "foto" : "img/lorena.jpg"},
        {"Nome": "Claudia", "Idade": "22 anos", "Posicao": "Goleira", "Naturalidade": "Pérola D'oeste - PR", "foto" : "img/claudia goleira.png"},
        {"Nome": "Camila", "Idade": "24 anos", "Posicao": "Goleira", "Naturalidade": "São Luís - MA", "foto" : "img/camila goleira.webp"},
        {"Nome": "Tarciane", "Idade": "22 anos", "Posicao": "Zagueira", "Naturalidade": "Belford roxo - RJ", "foto" : "img/tarciane.jpg"},
        {"Nome": "Antônia", "Idade": "31 anos", "Posicao": "Zagueira", "Naturalidade": "Riacho de Santana - RN", "foto" : "img/antonia zagueira.jpg"},
        {"Nome": "Isa Haass", "Idade": "24 anos", "Posicao": "Zagueira", "Naturalidade": "Monte Negro - MS", "foto" : "img/isa hass.jpeg"},
        {"Nome": "Kaká", "Idade": "25 anos", "Posicao": "Zagueira", "Naturalidade": "Brasília - DF", "foto" : "img/kaka.avif"},
        {"Nome": "Mariza", "Idade": "23 anos", "Posicao": "Zagueira", "Naturalidade": "Imperatriz - MA", "foto" : "img/mariza.jpg"},
        {"Nome": "Fê Parlemo", "Idade": "28 anos", "Posicao": "Lateral", "Naturalidade": "Campinas - SP", "foto" : "img/fe palermo.jpg"},
        {"Nome": "Yasmim", "Idade": "28 anos", "Posicao": "Lateral", "Naturalidade": "Governador Valadares - MG", "foto" : "img/yasmin.jpg"},
        {"Nome": "Fatima Dutra", "Idade": "25 anos", "Posicao": "Lateral", "Naturalidade": "Cedru - CE", "foto" : "img/fatima dutra.webp"},
        {"Nome": "Duda Sampaio", "Idade": "24 anos", "Posicao": "Meia-Campista", "Naturalidade": "Jequeri - MG", "foto" : "img/duda sampaio.jpg"},
        {"Nome": "Angelina", "Idade": "25 anos", "Posicao": "Meia-Campista", "Naturalidade": "Nova Jersey - EUA", "foto" : "img/Angelina.jpg"},
        {"Nome": "Ana Vitória", "Idade": "25 anos", "Posicao": "Meia-Campista", "Naturalidade": "Rondonopolis - MT", "foto" : "img/anavitoria.jpg"},
        {"Nome": "Ary Borges", "Idade": "25 anos", "Posicao": "Meia-Campista", "Naturalidade": "São Luís - MA", "foto" : "img/ary borges.jpg"},
        {"Nome": "Kerolin", "Idade": "25 anos", "Posicao": "Atacante", "Naturalidade": "Bauru - SP", "foto" : "img/kerolin.webp"},
        {"Nome": "Gio Queiroz", "Idade": "22 anos", "Posicao": "Atacante", "Naturalidade": "São Paulo - SP", "foto" : "img/gio queiroz.jpg"},
        {"Nome": "Luany", "Idade": "22 anos", "Posicao": "Atacante", "Naturalidade": "Nova Iguaçu - RJ", "foto" : "img/Luany.jpg"},
        {"Nome": "Dudinha", "Idade": "20 anos", "Posicao": "Atacante", "Naturalidade": "Itatiba - SP", "foto" : "img/dudinha.jpg"},
        {"Nome": "Marta", "Idade": "39 anos", "Posicao": "Atacante", "Naturalidade": "Dois Riacho - AL", "foto" : "img/marta.jpg"},
        {"Nome": "Amanda Gutierres", "Idade": "24 anos", "Posicao": "Atacante", "Naturalidade": "Querência - PR", "foto" : "img/amanda gutierres.webp"},
        {"Nome": "Gabi Portilho", "Idade": "29 anos", "Posicao": "Atacante", "Naturalidade": "Brasília - DF", "foto" : "img/gabi portilho.jpg"},
        {"Nome": "Jhonson", "Idade": "19 anos", "Posicao": "Atacante", "Naturalidade": "Londrina - PR", "foto" : "img/ingrid jhonson.webp"},

    ]
    context = {
        "jogadoras": jogadoras,
    }
    return render(request, "jogadoras.html", context)

def sobre(request):
    return render(request, "sobre.html")
