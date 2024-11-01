# api/models.py
from django.db import models

class PhoneNumber(models.Model):
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.number
