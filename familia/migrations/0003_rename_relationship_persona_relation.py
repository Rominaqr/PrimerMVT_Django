# Generated by Django 4.0.4 on 2022-05-17 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0002_persona_relationship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='relationship',
            new_name='relation',
        ),
    ]