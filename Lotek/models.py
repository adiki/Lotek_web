from __future__ import unicode_literals

from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    money = models.IntegerField(default=0)
    randoms = models.IntegerField(default=0)


