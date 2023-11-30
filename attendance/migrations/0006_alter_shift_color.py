# Generated by Django 4.0 on 2023-11-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_alter_shift_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='color',
            field=models.CharField(blank=True, choices=[('bg-primary', 'Blue'), ('bg-nfo', 'Light Blue'), ('bg-secondary', 'Gray'), ('bg-light', 'Light Gray'), ('bg-success', 'Green'), ('bg-danger', 'Red'), ('bg-dark', 'Black'), ('bg-warning', 'Yellow')], default='bg-light', max_length=100, null=True),
        ),
    ]
