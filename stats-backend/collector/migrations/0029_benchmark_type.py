# Generated by Django 3.2.12 on 2022-02-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0028_node_computing_now'),
    ]

    operations = [
        migrations.AddField(
            model_name='benchmark',
            name='type',
            field=models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary')], default='primary', max_length=9),
        ),
    ]
