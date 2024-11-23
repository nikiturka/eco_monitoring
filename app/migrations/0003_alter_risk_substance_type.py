# Generated by Django 5.1.3 on 2024-11-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_risk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='substance_type',
            field=models.CharField(choices=[('Carcinogenic', 'Carcinogenic'), ('Non-Carcinogenic', 'Non-Carcinogenic')], max_length=255),
        ),
    ]