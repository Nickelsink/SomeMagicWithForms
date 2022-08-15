from django.db import models


class Man(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    is_allowed = models.BooleanField(default=False)
