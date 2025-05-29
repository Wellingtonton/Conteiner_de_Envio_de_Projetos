from django.shortcuts import render

def lista_alunos(request):
    return render(request, 'alunos/lista_alunos.html')

def novo_aluno(request):
    return render(request, 'alunos/novo_aluno.html')

def detalhes_aluno(request, id):
    return render(request, 'alunos/detalhes_aluno.html', {'id': id})
