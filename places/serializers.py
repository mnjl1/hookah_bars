from rest_framework import serializers
from .models import Hookah, HookahImage, HookahTobacco
from rest_framework.reverse import reverse

class HookahTobaccoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HookahTobacco
        fields = (
            'hookah_tobacco',
        )

class HookahListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Hookah
        fields = (
            'id',
            'hookah_name',
            'city',
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

