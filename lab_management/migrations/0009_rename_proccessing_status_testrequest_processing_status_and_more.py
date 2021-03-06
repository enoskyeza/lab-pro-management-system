# Generated by Django 4.0.5 on 2022-06-27 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab_management', '0008_alter_sample_lab_reference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testrequest',
            old_name='proccessing_status',
            new_name='processing_status',
        ),
        migrations.AddField(
            model_name='sample',
            name='sample_id',
            field=models.CharField(default=None, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sample',
            name='date_of_collection',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sample',
            name='date_of_result',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='duration',
            field=models.FloatField(help_text='Enter test duration in hours i.e: 1.5 hours'),
        ),
    ]
