from django import forms
from .models import Pollutant, Enterprise, Record


class PollutantForm(forms.ModelForm):
    class Meta:
        model = Pollutant
        fields = ['pollutant_name', 'GDK_avg_daily', 'danger_class']


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['enterprise_name', 'enterprise_type', 'ownership', 'city', 'district']


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['year', 'enterprise', 'pollutant', 'emission_per_year']
