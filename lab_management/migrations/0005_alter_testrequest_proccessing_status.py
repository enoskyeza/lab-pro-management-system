# Generated by Django 4.0.5 on 2022-06-26 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_management', '0004_sample_testrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testrequest',
            name='proccessing_status',
            field=models.CharField(choices=[('STARTED', 'STARTED'), ('IN PROGRESS', 'IN PROGRESS'), ('COMPLETED', 'COMPLETED')], max_length=50),
        ),
    ]