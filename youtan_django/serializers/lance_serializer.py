from rest_framework import serializers

from youtan_django.core.models import Lance

class LanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lance
        fields = (
            'id',
            'created_by',
            'money_value',
            'deleted',
            'created_at',
            'updated_at',

            'get_leilao',
        )