from rest_framework import serializers

from core.models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = (
            'name',
            'slug',
            'leilao',
            'tipo_veiculo',
            'placa',
            'deleted',
            'created_at',
            'updated_at',

            'get_image',
            'get_thumbnail',
        )