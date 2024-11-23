from app.choices import TaxType


class TaxCalculatorFactory:
    @staticmethod
    def get_calculator(tax_type):
        calculators = {
            TaxType.atmosphere_tax: TaxCalculator.calculate_atmosphere_tax,
            TaxType.waterbody_tax: TaxCalculator.calculate_waterbody_tax,
            TaxType.placement_tax: TaxCalculator.calculate_placement_tax,
        }
        return calculators.get(tax_type)


class TaxCalculator:
    @staticmethod
    def calculate_atmosphere_tax(record):
        return record.emission_per_year * record.pollutant.atmosphere_tax

    @staticmethod
    def calculate_waterbody_tax(record):
        return record.emission_per_year * record.pollutant.waterbody_tax

    @staticmethod
    def calculate_placement_tax(record):
        return record.emission_per_year * record.pollutant.placement_tax