# Generated by Django 2.1.2 on 2018-11-07 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20181107_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='medical_date',
            field=models.CharField(default=5, max_length=4),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='vaccine_date',
            field=models.CharField(default=5, max_length=4),
        ),
    ]