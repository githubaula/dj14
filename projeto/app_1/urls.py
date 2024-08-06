from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('usuario_sucesso/', views.usuario_sucesso, name='usuario_sucesso'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefa_sucesso/', views.tarefa_sucesso, name='tarefa_sucesso'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('verificar_tarefas/<int:usuario_id>/', views.verificar_tarefas, name='verificar_tarefas'),
]