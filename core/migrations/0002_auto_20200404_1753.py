# Generated by Django 3.0.3 on 2020-04-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=13, primary_key=True, serialize=False),
        ),
    ]
