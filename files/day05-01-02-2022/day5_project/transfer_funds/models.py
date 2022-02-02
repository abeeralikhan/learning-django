from django.db import models

# Create your models here.

class Beneficiary(models.Model):
    name = models.CharField(max_length=20)
    account_no = models.IntegerField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class TranserFundsDetails(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)

