# Generated by Django 3.2.5 on 2021-07-25 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eptSN', '0004_auto_20210724_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='etudiant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscriptions', to='eptSN.etudiant'),
        ),
    ]
