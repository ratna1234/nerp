# -*- coding: utf-8 -*-
from rest_framework import serializers
from core.models import Party, Employee, Donor, Activity, Budget, TaxScheme


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
    name = serializers.Field(source='__str__')

    class Meta:
        model = Budget


class TaxSchemeSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='name')

    class Meta:
        model = TaxScheme