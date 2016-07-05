from rest_framework import serializers

from .models import Command



class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}


