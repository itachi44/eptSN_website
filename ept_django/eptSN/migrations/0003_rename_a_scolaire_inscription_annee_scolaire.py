# Generated by Django 3.2.5 on 2021-07-24 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eptSN', '0002_rename_annee_scolaire_inscription_a_scolaire'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscription',
            old_name='a_scolaire',
            new_name='annee_scolaire',
        ),
    ]
