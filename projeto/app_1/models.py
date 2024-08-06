from django.db import models

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tarefas')
    descricao = models.CharField(max_length=255)
    data = models.DateField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao