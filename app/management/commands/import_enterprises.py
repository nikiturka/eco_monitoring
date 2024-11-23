import os
import openpyxl
from django.core.management.base import BaseCommand
from app.models import Enterprise, ENTERPRISE_OWNERSHIP_CHOICES
from eco_monitoring.settings import BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file_path = os.path.join(BASE_DIR, 'data', 'enterprises.xlsx')

        try:
            wb = openpyxl.load_workbook(file_path)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                enterprise_id, enterprise_name, enterprise_type, ownership, city, district = row

                if ownership not in dict(ENTERPRISE_OWNERSHIP_CHOICES):
                    self.stdout.write(self.style.WARNING(f'Unknown ownership type: "{enterprise_name}"'))
                    continue

                enterprise, created = Enterprise.objects.get_or_create(
                    enterprise_name=enterprise_name,
                    defaults={
                        'enterprise_type': enterprise_type,
                        'ownership': ownership,
                        'city': city,
                        'district': district,
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'"{enterprise_name}" added'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'"{enterprise_name}" already exists'))

            self.stdout.write(self.style.SUCCESS('Enterprises imported successfully'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during import: {str(e)}'))