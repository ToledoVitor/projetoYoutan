from rest_framework import serializers

from core.models import Leilao

class BaseLeilaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leilao
        fields = (
            'item_type',
            'item_object',
            'item_id',
            'minimum_increment',
            'ended',
            'ended_at',
            'due_date',
            'get_latest_lance_value',
        )


class FullLeilaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leilao
        fields = (
            'item_type',
            'item_object',
            'item_id',
            'minimum_increment',
            'ended',
            'ended_at',
            'due_date',
            'entidade_financeira',
            'created_at',
            'updated_at',
            'get_latest_lance_value',
        )