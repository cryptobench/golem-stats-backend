# Generated by Django 3.2.4 on 2021-06-08 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0016_auto_20210519_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
