from django.db import models

class Tag(models.Model):
	desc = models.CharField(max_length=200)

class Transaction(models.Model):
	trans_date = models.DateTimeField('transaction date')
	comments = models.CharField(max_length=200)
	tag = models.ForeignKey(Tag)
	amount = models.IntegerField()
