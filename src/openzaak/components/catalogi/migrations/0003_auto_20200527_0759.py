# Generated by Django 2.2.10 on 2020-05-27 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogi", "0002_migrate_to_selectielijst_openzaak"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eigenschap",
            name="specificatie_van_eigenschap",
            field=models.ForeignKey(
                help_text="Attribuutkenmerken van de eigenschap",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalogi.EigenschapSpecificatie",
                verbose_name="specificatie van eigenschap",
            ),
        ),
    ]