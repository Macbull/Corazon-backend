from django.db import models

# Create your models here.

class Patient(models.Model):
	name = models.CharField(max_length = 40)
	aadhar_number = models.CharField(max_length = 13, unique = True)
	phone_number = models.CharField(max_length = 13)

class Checkup(models.Model):
	patient = models.ForeignKey(Patient)
	date = models.DateField(auto_now_add = True,auto_now = False)

class Sound(models.Model):
	checkup = models.ForeignKey(Checkup)
	created = models.DateTimeField(auto_now_add = True,auto_now = False)
	filename = models.CharField(max_length = 10)
