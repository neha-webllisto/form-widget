from django.db import models

# Create your models here.
class Widget_model(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()
	class1 = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	category = models.CharField(max_length=20)
	address = models.CharField(max_length=50)

