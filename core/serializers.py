from rest_framework import serializers
from core.models import Party, Employee, Donor, Activity, Budget


class PartySerializer(serializers.ModelSerializer):
    name = serializers.Field(source='name')

    class Meta:
        model = Party


class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='name')

    class Meta:
        model = Employee


class DonorSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='name')

    class Meta:
        model = Donor


class ActivitySerializer(serializers.ModelSerializer):
    name = serializers.Field(source='name')

    class Meta:
        model = Activity


class BudgetSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='name')

    class Meta:
        model = Budget