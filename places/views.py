from django.shortcuts import render
from rest_framework import generics
from .serializers import HookahListSerializer, HookahDetailSerializer
from .models import Hookah

class HookahListAPIView(generics.ListAPIView):
    queryset = Hookah.objects.all()
    serializer_class = HookahListSerializer

class HookahRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Hookah.objects.all()
    serializer_class = HookahDetailSerializer
