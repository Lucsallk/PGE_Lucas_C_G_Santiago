from rest_framework import serializers
from .models import Estagiario, Setor

class SetorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Setor
        fields = ['id', 'nome', 'chefe', 'capacidadeSetor']
        
class EstagiarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Estagiario       
        fields = ['id', 'nomeCompleto', 'cpf', 'dataNascimento', 'cursoGrad', 'instEnsino', 'cargaHoraria', 'setorAlocado']
    