from django.shortcuts import render

def lista_cursos(request):
    return render(request, 'cursos/lista_cursos.html')

def novo_curso(request):
    return render(request, 'cursos/novo_curso.html')

def detalhes_curso(request, id):
    # Aqui você irá buscar os detalhes do curso com o ID fornecido
    # Por enquanto, vamos apenas renderizar um template de detalhes
    return render(request, 'cursos/detalhes_curso.html', {'id': id})