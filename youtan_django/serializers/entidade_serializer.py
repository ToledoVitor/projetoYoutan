from rest_framework import serializers

from core.models import EntidadeFinanceira

class EntidadeFinanceiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadeFinanceira
        fields = (
            'name',
            'slug',
            'cnpj',
            'logradouro',
            'bairro',
            'numero',
            'cep',
            'cidade',
            'estado',
        )