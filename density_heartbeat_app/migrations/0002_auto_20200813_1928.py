# Generated by Django 3.1 on 2020-08-13 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('density_heartbeat_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='isalive',
            new_name='is_alive',
        ),
    ]
