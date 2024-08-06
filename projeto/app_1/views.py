from django.shortcuts import render, redirect
from .forms import UsuarioForm, TarefaForm
from .models import Usuario

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_sucesso')
    else:
        form = UsuarioForm()
    return render(request, 'criar_usuario.html', {'form': form})

def usuario_sucesso(request):
    return render(request, 'usuario_sucesso.html')

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefa_sucesso')
    else:
        form = TarefaForm()
    return render(request, 'criar_tarefa.html', {'form': form})

def tarefa_sucesso(request):
    return render(request, 'tarefa_sucesso.html')

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def verificar_tarefas(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    tarefas = usuario.tarefas.all()
    return render(request, 'verificar_tarefas.html', {'usuario': usuario, 'tarefas': tarefas})

def index(request):
    return render(request,'index.html')