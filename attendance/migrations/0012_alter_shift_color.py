# Generated by Django 4.0 on 2023-12-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_alter_shift_from_time_alter_shift_to_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='color',
            field=models.CharField(blank=True, choices=[('primary', 'Blue'), ('info', 'Light Blue'), ('secondary', 'Gray'), ('light', 'Light Gray'), ('success', 'Green'), ('success-l', 'Light Green'), ('danger', 'Red'), ('danger-l', 'Light Red'), ('warning', 'Yellow'), ('warning-l', 'Light Yellow'), ('dark', 'Black')], default='light', max_length=100, null=True),
        ),
    ]