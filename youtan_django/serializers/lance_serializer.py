from rest_framework import serializers

from core.models import Lance

class LanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lance
        fields = (
            'created_by',
            'leilao',
            'money_value',
            'deleted',
            'created_at',
            'updated_at',
        )