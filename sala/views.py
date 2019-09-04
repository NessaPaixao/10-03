from django.shortcuts import render
from rest_framework import viewsets
from sala.models import Aluno
from sala.serializers import AlunoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer



