# Generated by Django 4.0.5 on 2022-06-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
    ]
