from rest_framework import serializers
from .models import Contato

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['id', 'nome', 'telefone', 'email', 'criado_em', 'atualizado_em']
        read_only_fields = ['criado_em', 'atualizado_em']
    
    def validate_nome(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Nome deve ter pelo menos 2 caracteres.")
        return value.strip().title()

class ContatoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['id', 'nome', 'telefone', 'email']
