from django.db import models
import datetime

class Item(models.Model):
	title = models.CharField(max_length=250) 
	created_date = models.DateTimeField(default=datetime.datetime.now) 
	completed = models.BooleanField(default=False) 
	due = models.DateTimeField(default=datetime.datetime.now) 
 
	def __str__(self): 
		return self.title 
