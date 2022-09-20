from django.db import models
from django.contrib.auth.models import User

class Niveau(models.Model):
	id = models.AutoField(primary_key=True)
	nom = models.CharField(max_length=32)
	poid = models.FloatField()

	def __str__(self):
		return self.nom

class Employee(models.Model):
	id = models.AutoField(primary_key=True)
	nom = models.CharField(max_length=32)
	prenom = models.CharField(max_length=32)
	matricule = models.CharField(max_length=16)
	niveau = models.ForeignKey(Niveau, on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.nom} {self.prenom}"

class Presence(models.Model):
	id = models.BigAutoField(primary_key=True)
	date = models.DateField(auto_now_add=True)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	time_in = models.DateTimeField(auto_now_add=True, editable=False)
	time_out = models.DateTimeField(null=True)

class Conge(models.Model):
	id = models.AutoField(primary_key=True)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	debut = models.DateField()
	fin = models.DateField()
	payee = models.BooleanField(default=True)
