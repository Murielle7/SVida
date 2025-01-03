# Generated by Django 5.1.1 on 2024-11-21 01:18

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_datdate_recorded_vitalsign_date_recorded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalsign',
            name='blood_pressure',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='vitalsign',
            name='date_recorded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vitalsign',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient'),
        ),
        migrations.AlterField(
            model_name='vitalsign',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
