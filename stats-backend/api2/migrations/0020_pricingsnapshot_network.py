# Generated by Django 4.1.7 on 2024-02-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api2', '0019_pricingsnapshot_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingsnapshot',
            name='network',
            field=models.CharField(default='mainnet', max_length=42),
        ),
    ]
