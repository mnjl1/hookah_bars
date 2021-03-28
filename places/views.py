from django.shortcuts import render
from rest_framework import generics
from .serializers import HookahListSerializer, HookahDetailSerializer, HookahImageDetailSerializer
from .models import Hookah, HookahImage

class HookahListAPIView(generics.ListAPIView):
    queryset = Hookah.objects.all()
    serializer_class = HookahListSerializer

class HookahRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Hookah.objects.all()
    serializer_class = HookahDetailSerializer

class HookahImageRetrieveAPIView(generics.ListAPIView):
    queryset = HookahImage.objects.all()
    serializer_class = HookahImageDetailSerializer


class HookahCreateAPIView(generics.CreateAPIView):
    queryset = Hookah.objects.all()
    serializer_class = HookahDetailSerializer

class HookahRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Hookah.objects.all()
    serializer_class = HookahDetailSerializer


class HookahDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Hookah.objects.all()
