from rest_framework import serializers
from core.models import Party, Employee


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee