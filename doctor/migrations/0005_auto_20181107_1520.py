# Generated by Django 2.1.2 on 2018-11-07 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('doctor', '0004_auto_20181107_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('pet_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.mypet')),
                ('next_due', models.CharField(max_length=255)),
                ('time', models.CharField(default=5, max_length=4)),
                ('Description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='medical',
            name='medical_date',
            field=models.CharField(default=5, max_length=30),
        ),
    ]
