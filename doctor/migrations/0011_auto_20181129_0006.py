# Generated by Django 2.1.3 on 2018-11-28 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_auto_20181128_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='pet_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.mypet'),
        ),
    ]