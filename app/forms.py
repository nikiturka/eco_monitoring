from django import forms
from .models import Pollutant, Enterprise, Record, Tax


class PollutantForm(forms.ModelForm):
    class Meta:
        model = Pollutant
        fields = ['pollutant_name', 'GDK_avg_daily', 'danger_class', 'atmosphere_tax', 'placement_tax', 'waterbody_tax']


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['enterprise_name', 'enterprise_type', 'ownership', 'city', 'district']


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['year', 'enterprise', 'pollutant', 'emission_per_year']


class TaxForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = ['record', 'tax_type']
