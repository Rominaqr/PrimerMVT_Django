# Generated by Django 4.0.4 on 2022-05-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0004_remove_persona_relation'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='relation',
            field=models.CharField(default='', max_length=100),
        ),
    ]
