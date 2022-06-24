# Generated by Django 4.0.5 on 2022-06-24 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_management', '0003_alter_patient_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1),
        ),
    ]