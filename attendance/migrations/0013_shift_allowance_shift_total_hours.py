# Generated by Django 4.0 on 2023-12-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0012_alter_shift_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='allowance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shift',
            name='total_hours',
            field=models.IntegerField(default=8),
        ),
    ]
