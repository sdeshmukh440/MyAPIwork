from rest_framework import serializers
from .models import Language,Paradigm,Programmer




class LanguageSerializer(serializers.HyperlinkedModelSerializer):#To replace url with instance id import viewsets ModelSerializer
    class Meta:
        model=Language
        fields=('id','url','name','paradigm') #replace id with "url"


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id','url','name')


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id','url','name','languages')