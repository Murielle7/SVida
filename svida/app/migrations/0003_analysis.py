# Generated by Django 5.1.1 on 2024-11-19 01:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_vitalsign_recorded_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pressao_arterial', models.CharField(max_length=100)),
                ('temperatura', models.CharField(max_length=100)),
                ('frequencia_respiratoria', models.CharField(max_length=100)),
                ('frequencia_cardiaca', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
        ),
    ]