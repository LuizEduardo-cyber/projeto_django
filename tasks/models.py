from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField(blank = True)
    concluido = models.BooleanField(default = False)
    data_criacao = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.titulo