from rest_framework import serializers
from .models import Hookah, HookahImage

class HookahListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hookah
        fields = [
            'id',
            'hookah_name',
            'city',
        ]


class HookahImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HookahImage
        fields = (
            'hookah_image',
        )


class HookahDetailSerializer(serializers.ModelSerializer):
    hookah_images = HookahImageDetailSerializer(many = True)
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
            'summer_terrace',
            'hookah_images'
        ]
    def create(self, validated_data):
        images_data = validated_data.pop(**validated_data)
        hookah = Hookah.objects.create(**validated_data)
        for image_data in images_data:
            Hookah.objects.create(hookah = hookah, **image_data)
        return hookah

