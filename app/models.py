from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from app.choices import ENTERPRISE_OWNERSHIP_CHOICES


class Pollutant(models.Model):
    pollutant_name = models.CharField(max_length=255, unique=True)
    chemical_formula = models.CharField(max_length=50)
    GDK_avg_daily = models.FloatField(validators=[MinValueValidator(0)])
    danger_class = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    def __str__(self):
        return self.pollutant_name


class Enterprise(models.Model):
    enterprise_name = models.CharField(max_length=255, unique=True)
    enterprise_type = models.CharField(max_length=255)
    ownership = models.CharField(max_length=255, choices=ENTERPRISE_OWNERSHIP_CHOICES)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)

    def __str__(self):
        return self.enterprise_name


class Record(models.Model):
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name='records')
    pollutant = models.ForeignKey(Pollutant, on_delete=models.CASCADE, related_name='records')
    emission_per_year = models.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('year', 'enterprise', 'pollutant')

    def __str__(self):
        return f"Record for {self.enterprise} in {self.year}"
