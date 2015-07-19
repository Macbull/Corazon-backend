from operater.models import *
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient

class CheckupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Checkup

class SoundSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sound
