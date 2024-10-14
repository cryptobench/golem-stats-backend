# Generated by Django 4.1.7 on 2024-09-24 12:00

from django.db import migrations
from django.db.models import F

def cleanup_nodestatushistory(apps, schema_editor):
    NodeStatusHistory = apps.get_model('api2', 'NodeStatusHistory')
    
    # Get all node_ids
    node_ids = NodeStatusHistory.objects.values_list('node_id', flat=True).distinct()

    for node_id in node_ids:
        entries = NodeStatusHistory.objects.filter(node_id=node_id).order_by('timestamp')
        previous_status = None
        to_delete = []

        for entry in entries:
            if previous_status is not None and entry.is_online == previous_status:
                to_delete.append(entry.id)
            else:
                previous_status = entry.is_online

        # Delete duplicate entries for this node
        NodeStatusHistory.objects.filter(id__in=to_delete).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('api2', '0035_remove_nodestatushistory_api2_nodest_provide_64b3a2_idx'),
    ]

    operations = [
        migrations.RunPython(cleanup_nodestatushistory),
    ]