from rest_framework import serializers
from training.models import Participant, Organization, File


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization


class ParticipantSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Participant


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File