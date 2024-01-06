from django.db import models


# Create your models here.
class data(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=800, null=True, blank=True)
    address = models.CharField(max_length=800, null=True, blank=True)
