from dataclasses import fields
from rest_framework import serializers
from .models import Becario


class BecarioSerializer (serializers.ModelSerializer):

    class Meta:
        model = Becario
        fields = '__all__'