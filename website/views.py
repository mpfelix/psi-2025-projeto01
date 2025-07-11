from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadoras(request):
    jogadoras = [
        
    ]
    context = {
        "jogadoras": jogadoras,
    }
    return render(request, "jogadoras.html", context)

def sobre(request):
    return render(request, "sobre.html")
