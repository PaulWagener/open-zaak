# Generated by Django 2.2.9 on 2020-01-03 15:11
from django.apps import apps as _real_apps
from django.contrib.auth.management import create_permissions
from django.core.management import call_command
from django.db import migrations


def forward(apps, schema_editor):
    for app_config in _real_apps.app_configs.values():
        create_permissions(app_config, verbosity=0, interactive=False)

    call_command("loaddata", "default_groups.json")


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_initial_admin_index"),
        ("auth", "0001_initial"),
        ("sites", "0001_initial"),
        ("vng_api_common", "0002_apicredential"),
        ("authorizations", "0001_initial"),
        ("audittrails", "0001_initial"),
        ("notifications", "0001_initial"),
        ("autorisaties", "0001_initial"),
        ("notifications_log", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forward, migrations.RunPython.noop),
    ]
