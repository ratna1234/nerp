from rest_framework import serializers
from core.models import Party, Employee, Donor, Activity


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity