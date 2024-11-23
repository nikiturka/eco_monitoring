import os
import openpyxl
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from app.models import Pollutant, Risk
from eco_monitoring.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Import risks from XLSX file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(BASE_DIR, 'data', 'risks.xlsx')

        try:
            wb = openpyxl.load_workbook(file_path)
            sheet = wb.active

            sheet.delete_cols(10)

            for row in sheet.iter_rows(min_row=2, values_only=True):
                (
                    risk_id,
                    pollutant_name,
                    substance_type,
                    danger_class,
                    gdk,
                    concentration,
                    rfc,
                    sfi,
                    current_risk
                ) = row

                # Обработка значений: пустые строки превращаем в None
                gdk = float(gdk) if gdk else None
                concentration = float(concentration) if concentration else None
                rfc = float(rfc) if rfc else None
                sfi = float(sfi) if sfi else None
                current_risk = current_risk.strip() if current_risk else None

                pollutant = get_object_or_404(Pollutant, pollutant_name=pollutant_name)

                risk, created = Risk.objects.get_or_create(
                    pollutant=pollutant,
                    defaults={
                        'substance_type': substance_type,
                        'danger_class': int(danger_class),
                        'gdk': gdk,
                        'concentration': concentration,
                        'rfc': rfc,
                        'sfi': sfi,
                        'current_risk': current_risk,
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Risk for "{pollutant_name}" added'))
                else:
                    self.stdout.write(self.style.WARNING(f'Risk for "{pollutant_name}" already exists'))

            self.stdout.write(self.style.SUCCESS('Risks imported successfully'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during import: {str(e)}'))