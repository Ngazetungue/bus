from enum import unique
from unicodedata import name
from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=60
    )
    description = models.TextField(
        null=False,
        blank=False,
        max_length=2500
    )
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name

class Bus(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=60
    )
    description = models.TextField(
        null=False,
        blank=False,
        max_length=2500
    )
    destination = models.ManyToManyField(
        Destination,
        related_name="destinations"
    )

    def __str__(self) -> str:
        return self.name