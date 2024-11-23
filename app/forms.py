from django import forms

from .choices import TAX_TYPE_CHOICES
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


class TaxForm(forms.Form):
    tax_type = forms.ChoiceField(choices=TAX_TYPE_CHOICES, label="Тип таксу")

    def save(self, record):
        tax_type = self.cleaned_data['tax_type']

        tax = Tax.objects.create(
            record=record,
            tax_type=tax_type,
        )
        return tax
