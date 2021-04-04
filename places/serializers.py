from rest_framework import serializers
from .models import Hookah, HookahImage, HookahTobacco, HookahType
from cities_light.models import City
from rest_framework.reverse import reverse

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'name',
        ]

class HookahTobaccoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HookahTobacco
        fields = (
            'hookah_tobacco',
        )

class HookahTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HookahType
        fields = (
            'hookah_type',
        )

class HookahListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()
    city = CitySerializer(many = False)
    class Meta:
        model = Hookah
        fields = (
            'id',
            'hookah_name',
            'city',
            'street',
            'absolute_url',
        )
    
    def get_absolute_url(self, obj):
        return reverse('hookah_detail', args = (obj.pk,))


class HookahImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HookahImage
        fields = (
            'id',
            'hookah_image',
        )


class HookahDetailSerializer(serializers.ModelSerializer):
    hookah_images = HookahImageDetailSerializer(many = True)
    hookah_tobacco = HookahTobaccoDetailSerializer(many = True, read_only = True)
    hookah_type = HookahTypeDetailSerializer(many = True, read_only = True)
    city = CitySerializer(many = False)
    class Meta:
        model = Hookah
        fields = (
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
        )

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('hookah_images')
        hookah = Hookah.objects.create(**validated_data)
        for image_data in images_data:
            Hookah.objects.create(hookah = hookah, **image_data)
        return hookah

