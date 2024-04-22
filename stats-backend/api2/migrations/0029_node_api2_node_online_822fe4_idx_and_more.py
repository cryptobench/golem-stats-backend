# Generated by Django 4.1.7 on 2024-04-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api2', '0028_node_earnings_total'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='node',
            index=models.Index(fields=['online', 'computing_now'], name='api2_node_online_822fe4_idx'),
        ),
        migrations.AddIndex(
            model_name='node',
            index=models.Index(fields=['network', 'online'], name='api2_node_network_130c4f_idx'),
        ),
        migrations.AddIndex(
            model_name='offer',
            index=models.Index(fields=['provider', 'runtime'], name='api2_offer_provide_48a686_idx'),
        ),
        migrations.AddIndex(
            model_name='offer',
            index=models.Index(fields=['is_overpriced', 'overpriced_compared_to'], name='api2_offer_is_over_a57eb1_idx'),
        ),
        migrations.AddIndex(
            model_name='offer',
            index=models.Index(fields=['cheaper_than'], name='api2_offer_cheaper_05ab5b_idx'),
        ),
    ]