from rest_framework import serializers
from training.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
