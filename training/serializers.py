from rest_framework import serializers
from training.models import Participant, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization


class ParticipantSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Participant


