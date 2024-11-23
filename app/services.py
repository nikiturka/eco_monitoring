from app.choices import TaxType, SubstanceType


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


class RiskCalculatorFactory:
    @staticmethod
    def get_calculator(substance_type):
        calculators = {
            SubstanceType.carcinogenic: RiskCalculator.calculate_carcinogenic_risk,
            SubstanceType.non_carcinogenic: RiskCalculator.calculate_non_carcinogenic_risk,
        }
        return calculators.get(substance_type)


class RiskCalculator:
    @staticmethod
    def calculate_non_carcinogenic_risk(risk):
        if risk.concentration == 0:
            return 'дуже малий'
        return risk.concentration / risk.rfc if risk.concentration else 0

    @staticmethod
    def calculate_carcinogenic_risk(risk):
        if risk.concentration == 0:
            return 'дуже малий'
        ladd = (risk.concentration * 20 * 365 * 70) / (70 * 70 * 365)
        return ladd / risk.sfi if risk.sfi else ladd
