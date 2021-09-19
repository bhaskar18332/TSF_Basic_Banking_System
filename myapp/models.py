from django.db import models

# Create your models here.

class Users(models.Model):
	name =  models.CharField(max_length=100)
	balance = models.IntegerField()
	email = models.EmailField(max_length=254)

	def __str__(self):
		return self.name

class transactions(models.Model):
	name1 = models.CharField(max_length=100)
	name2 = models.CharField(max_length=100)
	amount  = models.IntegerField()
	
	def __str__(self):
		return self.name1+' '+self.name2