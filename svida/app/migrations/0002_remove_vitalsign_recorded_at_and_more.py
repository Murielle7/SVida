# Generated by Django 5.1.1 on 2024-11-07 02:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vitalsign',
            name='recorded_at',
        ),
        migrations.AlterField(
            model_name='vitalsign',
            name='blood_pressure',
            field=models.CharField(help_text='Pressão Arterial (ex: 120/80 mmHg)', max_length=7),
        ),
        migrations.AlterField(
            model_name='vitalsign',
            name='breath_rate',
            field=models.IntegerField(help_text='Frequência Respiratória (rpm)'),
        ),
        migrations.AlterField(
            model_name='vitalsign',
            name='heart_rate',
            field=models.IntegerField(help_text='Frequência Cardíaca (bpm)'),
        ),
        migrations.AlterField(
            model_name='vitalsign',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vital_signs', to='app.patient'),
        ),
        migrations.AlterField(
            model_name='vitalsign',
            name='temperature',
            field=models.DecimalField(decimal_places=2, help_text='Temperatura (°C)', max_digits=5),
        ),
    ]