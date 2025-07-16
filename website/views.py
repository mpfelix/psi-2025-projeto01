from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadoras(request):
    jogadoras = [
        {"Nome": "Lorena", "Idade": "28 anos", "Posicao": "Goleira", "Naturalidade": "Ituverava - SP", "foto" : "lorena.jpg"},
        {"Nome": "Claudia", "Idade": "22 anos", "Posicao": "Goleira", "Naturalidade": "Pérola D'oeste - PR", "foto" : "claudia goleira.jpg"},
        {"Nome": "Camila", "Idade": "24 anos", "Posicao": "Goleira", "Naturalidade": "São Luís - MA", "foto" : "camila goleira.jpg"},
        {"Nome": "Tarciane", "Idade": "22 anos", "Posicao": "Zagueira", "Naturalidade": "Belford roxo - RJ", "foto" : "tarciane.jpg"},
        {"Nome": "Antônia", "Idade": "31 anos", "Posicao": "Zagueira", "Naturalidade": "Riacho de Santana - RN", "foto" : "antonia zagueira.jpg"},
        {"Nome": "Isa Haass", "Idade": "24 anos", "Posicao": "Zagueira", "Naturalidade": "Monte Negro - MS", "foto" : "isa haass.jpg"},
        {"Nome": "Kaká", "Idade": "25 anos", "Posicao": "Zagueira", "Naturalidade": "Brasília - DF", "foto" : "kaka.jpg"},
        {"Nome": "Mariza", "Idade": "23 anos", "Posicao": "Zagueira", "Naturalidade": "Imperatriz - MA", "foto" : "mariza.jpg"},
        {"Nome": "Fê Parlemo", "Idade": "28 anos", "Posicao": "Lateral", "Naturalidade": "Campinas - SP", "foto" : "fe parlemo.jpg"},
        {"Nome": "Yasmim", "Idade": "28 anos", "Posicao": "Lateral", "Naturalidade": "Governador Valadares - MG", "foto" : "yasmim.jpg"},
        {"Nome": "Fatima Dutra", "Idade": "25 anos", "Posicao": "Lateral", "Naturalidade": "Cedru - CE", "foto" : "fatiama dutra.jpg"},
        {"Nome": "Duda Sampaio", "Idade": "24 anos", "Posicao": "Meia-Campista", "Naturalidade": "Jequeri - MG", "foto" : "fatiama dut.jpg"},
        {"Nome": "Angelina", "Idade": "25 anos", "Posicao": "Meia-Campista", "Naturalidade": "Nova Jersey - EUA", "foto" : "Angelina.jpg"},
        {"Nome": "Ana Vitória", "Idade": "25 anos", "Posicao": "Meia-Campista", "Naturalidade": "Rondonopolis - MT", "foto" : "ana vitoria.jpg"},
        {"Nome": "Ary Borges", "Idade": "25 anos", "Posicao": "Meia-Campista", "Naturalidade": "São Luís - MA", "foto" : "ary borges.jpg"},
        {"Nome": "Kerolin", "Idade": "25 anos", "Posicao": "Atacante", "Naturalidade": "Bauru - SP", "foto" : "kerolin.jpg"},
        {"Nome": "Gio Queiroz", "Idade": "22 anos", "Posicao": "Atacante", "Naturalidade": "São Paulo - SP", "foto" : "gio queiroz.jpg"},
        {"Nome": "Luany", "Idade": "22 anos", "Posicao": "Atacante", "Naturalidade": "Nova Iguaçu - RJ", "foto" : "Luany.jpg"},
        {"Nome": "Dudinha", "Idade": "20 anos", "Posicao": "Atacante", "Naturalidade": "Itatiba - SP", "foto" : "dudinha.jpg"},
        {"Nome": "Marta", "Idade": "39 anos", "Posicao": "Atacante", "Naturalidade": "Dois Riacho - AL", "foto" : "marta.jpg"},
        {"Nome": "Amanda Gutierres", "Idade": "24 anos", "Posicao": "Atacante", "Naturalidade": "Querência - PR", "foto" : "amanda gutierres.jpg"},
        {"Nome": "Gabi Portilho", "Idade": "29 anos", "Posicao": "Atacante", "Naturalidade": "Brasília - DF", "foto" : "gabi portilho.jpg"},
        {"Nome": "Jhonson", "Idade": "19 anos", "Posicao": "Atacante", "Naturalidade": "Londrina - PR", "foto" : "jhonson.jpg"},

    ]
    context = {
        "jogadoras": jogadoras,
    }
    return render(request, "jogadoras.html", context)

def sobre(request):
    return render(request, "sobre.html")
