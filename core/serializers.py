# -*- coding: utf-8 -*-
from rest_framework import serializers
from core.models import Party, Employee, Donor, Activity, BudgetHead, TaxScheme, BudgetBalance


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


class BudgetBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetBalance


class BudgetSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='__str__')
    current_balance = BudgetBalanceSerializer()

    class Meta:
        model = BudgetHead
        exclude = ['id', 'budget_head']


class TaxSchemeSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='name')

    class Meta:
        model = TaxScheme