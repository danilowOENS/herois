from rest_framework import serializers
from herois.models import  Herois



class HeroisSerializers(serializers.ModelSerializer):
    nome = serializers.CharField(read_only=True)

class HeroiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255,required=True)
