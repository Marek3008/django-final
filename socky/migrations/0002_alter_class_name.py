# Generated by Django 4.2.13 on 2024-05-31 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socky', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=6),
        ),
    ]
