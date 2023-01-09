from rest_framework import serializers

from youtan_django.core.models import Leilao

class LeilaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leilao
        fields = (
            'id',
            'minimum_increment',
            'ended',
            'ended_at',
            'due_date',

            'created_at',
            'updated_at',

            'get_latest_lance_value',
            'get_item_type',
            'get_item_object',
            'get_entidade_financeira',
        )