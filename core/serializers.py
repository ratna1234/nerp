from rest_framework import serializers
from core.models import Party


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
