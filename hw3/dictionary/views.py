# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from . import forms
from . import models

class EnViewSet(viewsets.ModelViewSet):
    queryset = models.Word.objects.all()
    serializer_class = forms.WordsSerializer

    def get_queryset(self):
        return models.Word.objects.filter(language='en')

class RuViewSet(viewsets.ModelViewSet):
    queryset = models.Word.objects.all()
    serializer_class = forms.WordsSerializer

    def get_queryset(self):
        return models.Word.objects.filter(language='ru')

class KzViewSet(viewsets.ModelViewSet):
    queryset = models.Word.objects.all()
    serializer_class = forms.WordsSerializer

    def get_queryset(self):
        return models.Word.objects.filter(language='kz')

class EnDetailViewSet(viewsets.ModelViewSet):
    queryset = models.Word.objects.all()
    serializer_class = forms.WordsDetailSerializer

    def get_queryset(self):
        return models.Word.objects.filter(language='en')

class RuDetailViewSet(viewsets.ModelViewSet):
    queryset = models.Word.objects.all()
    serializer_class = forms.WordsDetailSerializer

    def get_queryset(self):
        return models.Word.objects.filter(language='ru')

class KzDetailViewSet(viewsets.ModelViewSet):
    queryset = models.Word.objects.all()
    serializer_class = forms.WordsDetailSerializer

    def get_queryset(self):
        return models.Word.objects.filter(language='kz')




