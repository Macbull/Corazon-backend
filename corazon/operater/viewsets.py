from operater.models import *
from rest_framework import viewsets
from operater.serializers import *

class PatientViewSet(viewsets.ModelViewSet):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer

class CheckupViewSet(viewsets.ModelViewSet):
	queryset = Checkup.objects.all()
	serializer_class = CheckupSerializer

class SoundViewSet(viewsets.ModelViewSet):
	queryset = Sound.objects.all()
	serializer_class = SoundSerializer
