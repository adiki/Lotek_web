from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Result(models.Model):
    date = models.DateTimeField()
    number = models.IntegerField()
