from django.shortcuts import render
from rest_framework import viewsets,permissions

from .models import Language,Paradigm,Programmer
from .serializers import LanguageSerializer,ParadigmSerializer,ProgrammerSerializer

#WE CAN APPLLY GLOBAL(ALL VIEW CLASSESS) PERMISSION FROM SETTINGS.PY OR WE CAN DO IT FOR SPECIFIC View CLASS

""" Login credientials are 'username=sd', 'password=1234 """

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #FOR SPECIFIC View class

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer