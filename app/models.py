from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from app.choices import ENTERPRISE_OWNERSHIP_CHOICES, TAX_TYPE_CHOICES, TaxType, SUBSTANCE_TYPE_CHOICES


class Pollutant(models.Model):
    pollutant_name = models.CharField(max_length=255, unique=True)
    atmosphere_tax = models.FloatField(validators=[MinValueValidator(0)])
    waterbody_tax = models.FloatField(validators=[MinValueValidator(0)])
    placement_tax = models.FloatField(validators=[MinValueValidator(0)])
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

    def __str__(self):
        return f"Record for {self.enterprise} in {self.year} on {self.pollutant}"


class Tax(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    tax_amount = models.FloatField(validators=[MinValueValidator(0)])
    tax_type = models.CharField(max_length=255, choices=TAX_TYPE_CHOICES)

    def __str__(self):
        return f'{self.tax_type} for {self.record.enterprise} in {self.record.year}'

    @property
    def pollutant_tax_type_value(self):
        tax_mapping = {
            TaxType.atmosphere_tax: self.record.pollutant.atmosphere_tax,
            TaxType.waterbody_tax: self.record.pollutant.waterbody_tax,
            TaxType.placement_tax: self.record.pollutant.placement_tax,
        }
        return tax_mapping.get(self.tax_type)


class Risk(models.Model):
    pollutant = models.ForeignKey(Pollutant,on_delete=models.CASCADE)
    substance_type = models.CharField(max_length=255, choices=SUBSTANCE_TYPE_CHOICES)
    danger_class = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    gdk = models.FloatField(validators=[MinValueValidator(0)], null=True, blank=True)
    concentration = models.FloatField(validators=[MinValueValidator(0)], null=True, blank=True)
    rfc = models.FloatField(validators=[MinValueValidator(0)], null=True, blank=True)
    sfi = models.FloatField(validators=[MinValueValidator(0)], null=True, blank=True)
    current_risk = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Risk for {self.pollutant}"
