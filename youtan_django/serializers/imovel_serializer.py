from rest_framework import serializers

from youtan_django.core.models import Imovel

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = (
            'id',
            'name',
            'tipo_imovel',
            'logradouro',
            'bairro',
            'numero',
            'cep',
            'cidade',
            'estado',

            'deleted',
            'created_at',
            'updated_at',

            'get_image',
            'get_thumbnail',
        )