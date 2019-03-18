from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length = 30)
	college = models.CharField(max_length = 50)
	age = models.IntegerField()
	phone_no = models.CharField(max_length = 30)
	
class employee (models.Model):
	name = models.CharField(max_length = 30)
	age = models.IntegerField()
	phone_no = models.CharField(max_length = 30)
	salary = models.CharField(max_length = 30)
	
	