# Generated by Django 2.1.2 on 2018-11-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='medical_date',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='vaccine_date',
            field=models.CharField(max_length=255),
        ),
    ]