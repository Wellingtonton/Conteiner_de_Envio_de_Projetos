from django.http import HttpResponse

def lista_fichas(request):
    return HttpResponse("<h1>Lista de Fichas</h1>")

def nova_ficha(request):
    return HttpResponse("<h1>Criar nova Ficha</h1>")

def detalhes_ficha(request, id):
    return HttpResponse(f"<h1>Detalhes da Ficha ID: {id}</h1>")



