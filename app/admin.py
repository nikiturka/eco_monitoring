from django.contrib import admin
from .models import Enterprise, Pollutant, Record, Tax

admin.site.register(Enterprise)
admin.site.register(Pollutant)
admin.site.register(Record)
admin.site.register(Tax)