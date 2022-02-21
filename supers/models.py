from django.db import models
from super_types.models import Super_types

# Create your models here.
class Supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    second_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(Super_types, on_delete=models.CASCADE)

    def __str__(self):
        return self.type