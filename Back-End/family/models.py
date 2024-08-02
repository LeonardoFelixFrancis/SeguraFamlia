from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Family(models.Model):

    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.surname} Family'