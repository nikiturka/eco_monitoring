from django import forms
from .models import Pollutant

class PollutantForm(forms.ModelForm):
    class Meta:
        model = Pollutant
        fields = ['pollutant_name', 'chemical_formula', 'GDK_avg_daily', 'danger_class']
