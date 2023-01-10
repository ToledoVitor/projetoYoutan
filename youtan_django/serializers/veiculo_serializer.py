from rest_framework import serializers

from youtan_django.core.models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = (
            'id',
            'name',
            'tipo_veiculo',
            'placa',
            'ano',
            'deleted',
            'created_at',
            'updated_at',

            'get_image',
            'get_thumbnail',
        )