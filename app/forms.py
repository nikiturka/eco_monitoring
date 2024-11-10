from django import forms
from .models import Pollutant, Enterprise


class PollutantForm(forms.ModelForm):
    class Meta:
        model = Pollutant
        fields = ['pollutant_name', 'chemical_formula', 'GDK_avg_daily', 'danger_class']


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['enterprise_name', 'enterprise_type', 'ownership', 'city', 'district']
