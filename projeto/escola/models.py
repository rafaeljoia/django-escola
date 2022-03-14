from django.db import models

# Create your models here.
from account.models import Aluno


class Turma(models.Model):
    nome_turma = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_turma

class TurmaAluno(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ManyToManyField(Aluno)


    def __str__(self):
        return self.turma.nome_turma
