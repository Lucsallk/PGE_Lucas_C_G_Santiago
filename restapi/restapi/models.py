from django.db import models
from cpf_field.models import CPFField

# talvez eu precise remover a uniquicidade de cpf por agora
class Estagiario(models.Model):
    nomeCompleto = models.CharField(max_length=220)
    cpf = CPFField(max_length=11)
    dataNascimento = models.DateField()
    cursoGrad = models.CharField(max_length=120)
    instEnsino = models.CharField(max_length=220)
    cargaHoraria = models.SmallIntegerField()
    setorAlocado = models.CharField(max_length=120)

    def __str__(self):
        return self.nomeCompleto

class Setor(models.Model):
    nome = models.CharField(max_length=220)
    chefe = models.CharField(max_length=200)
    capacidadeSetor = models.SmallIntegerField()
    
    def __str__(self):
        return self.nome
        