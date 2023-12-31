# Generated by Django 4.0 on 2023-11-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='color',
            field=models.CharField(blank=True, choices=[('bg-primary', 'Primary'), ('bg-info', 'Info'), ('bg-secondary', 'Secondary'), ('bg-light', 'Light'), ('bg-success', 'Success'), ('bg-danger', 'Danger'), ('bg-dark', 'Dark'), ('bg-warning', 'Warning')], default='bg-light', max_length=100, null=True),
        ),
    ]
