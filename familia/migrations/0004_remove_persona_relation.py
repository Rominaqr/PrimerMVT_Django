# Generated by Django 4.0.4 on 2022-05-17 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0003_rename_relationship_persona_relation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='relation',
        ),
    ]
