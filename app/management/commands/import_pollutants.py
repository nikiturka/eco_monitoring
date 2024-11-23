import os
import openpyxl
from django.core.management.base import BaseCommand
from eco_monitoring.settings import BASE_DIR
from app.models import Pollutant

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            wb = openpyxl.load_workbook(file_path)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                (
                    pollutant_id, pollutant_name, atmosphere_tax,
                    waterbody_tax, placement_tax, GDK_avg_daily,
                    danger_class
                ) = row

                if isinstance(GDK_avg_daily, str) and '<' in GDK_avg_daily:
                    GDK_avg_daily = float(GDK_avg_daily.replace('<', '').replace(',', '.'))

                atmosphere_tax = float(str(atmosphere_tax).replace(',', '.'))
                waterbody_tax = float(str(waterbody_tax).replace(',', '.'))
                placement_tax = float(str(placement_tax).replace(',', '.'))

                pollutant, created = Pollutant.objects.get_or_create(
                    pollutant_name=pollutant_name,
                    defaults={
                        'atmosphere_tax': atmosphere_tax,
                        'waterbody_tax': waterbody_tax,
                        'placement_tax': placement_tax,
                        'GDK_avg_daily': GDK_avg_daily,
                        'danger_class': danger_class,
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'"{pollutant_name}" added'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'"{pollutant_name}" already exists'))

            self.stdout.write(self.style.SUCCESS('Pollutants imported'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during import: {str(e)}'))