from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *

class TokenPairSerializer(TokenObtainPairSerializer):
    pass

class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model=Niveau
        fields= "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields= "__all__"

class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Presence
        fields= "__all__"
class CongeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Conge
        fields= "__all__"