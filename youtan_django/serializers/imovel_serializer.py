from rest_framework import serializers

from core.models import Imovel

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = (
            'name',
            'slug',
            'leilao',
            'tipo_imovel',
            'placa',
            'deleted',
            'created_at',
            'updated_at',

            'get_image',
            'get_thumbnail',
        )