# Generated by Django 2.0.7 on 2018-11-07 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('createStaff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='firstname',
            new_name='name',
        ),
    ]
