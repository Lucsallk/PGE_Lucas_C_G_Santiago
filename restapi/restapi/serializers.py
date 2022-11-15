from rest_framework import serializers
from .models import Estagiario, Setor

class EstagiarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Estagiario
        fields = ['id', 'nomeCompleto', 'dataNascimento', 'cursoGrad', 'instEnsino', 'cargaHoraria', 'setorAlocado']
        #fiels = '__all__'

class EditEstagiarioSerializer(serializers.ModelSerializer):
    model = Estagiario
    fields = ['id', 'nomeCompleto', 'dataNascimento', 'cursoGrad', 'instEnsino', 'cargaHoraria', 'setorAlocado']

class SetorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Setor
        fields = ['id', 'nome', 'chefe', 'capacidadeSetor']