from django.http import HttpResponse

def lista_treinos(request):
    return HttpResponse("<h1>Lista de Treinos</h1>")

def novo_treino(request):
    return HttpResponse("<h1>Criar Novo Treino</h1>")

def detalhes_treino(request, id):
    return HttpResponse(f"<h1>Detalhes do Treino ID: {id}</h1>")
    
    


