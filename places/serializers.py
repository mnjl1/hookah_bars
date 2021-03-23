from rest_framework import serializers
from .models import Hookah

class HookahListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hookah
        fields = [
            'id',
            'hookah_name',
            'city',
        ]


class HookahDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hookah
        fields = [
            'id',
            'hookah_name',
            'city',
            'street',
            'website',
            'phone',
            'description',
            'credit_card',
            'hookah_type',
            'hookah_tobacco',
            'summer_terrace'
        ]