from rest_framework import serializers

from youtan_django.core.models import EntidadeFinanceira

class EntidadeFinanceiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadeFinanceira
        fields = (
            'id',
            'name',
            'cnpj',
        )