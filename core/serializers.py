# -*- coding: utf-8 -*-
from rest_framework import serializers
from core.models import Party, Employee, Donor, Activity, BudgetHead, TaxScheme, BudgetBalance, Language


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
        exclude = ['id', 'budget_head', 'fiscal_year', 'nepal_government', 'foreign_cash_grant', 'foreign_cash_loan',
                   'foreign_compensating_grant', 'foreign_compensating_loan', 'foreign_substantial_aid']


class BudgetSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='__str__')
    current_balance = BudgetBalanceSerializer()

    class Meta:
        model = BudgetHead


class TaxSchemeSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='name')

    class Meta:
        model = TaxScheme

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model= Language