# Generated by Django 3.2.4 on 2021-06-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0021_alter_requestors_tasks_requested'),
    ]

    operations = [
        migrations.CreateModel(
            name='requestor_scraper_check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indexed_before', models.BooleanField(default=False)),
            ],
        ),
    ]