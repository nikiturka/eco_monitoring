import os
import openpyxl
from django.core.management.base import BaseCommand
from eco_monitoring.settings import BASE_DIR
from app.models import Record, Pollutant, Enterprise

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file_path = os.path.join(BASE_DIR, 'data', 'records.xlsx')

        try:
            wb = openpyxl.load_workbook(file_path, data_only=True)  # data_only=True, to get formula results
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                record_id, year, enterprise_name, pollutant_name, emission_per_year = row

                try:
                    emission_per_year = float(emission_per_year)
                except (ValueError, TypeError):
                    self.stdout.write(self.style.ERROR(f'invalid emission type {record_id}: "{emission_per_year}"'))
                    continue

                try:
                    enterprise = Enterprise.objects.get(enterprise_name=enterprise_name)
                except Enterprise.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Предприятие "{enterprise_name}" не найдено'))
                    continue

                try:
                    pollutant = Pollutant.objects.get(pollutant_name=pollutant_name)
                except Pollutant.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Загрязнитель "{pollutant_name}" не найден'))
                    continue

                record, created = Record.objects.get_or_create(
                    year=year,
                    enterprise=enterprise,
                    pollutant=pollutant,
                    defaults={'emission_per_year': emission_per_year}
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Record for "{enterprise_name}" and "{pollutant_name}" in {year} added'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Record for "{enterprise_name}" and "{pollutant_name}" in {year}already exists'))

            self.stdout.write(self.style.SUCCESS('Pollutants imported'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during import: {str(e)}'))