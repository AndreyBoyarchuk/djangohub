# Generated by Django 4.1.2 on 2022-11-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone_number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
