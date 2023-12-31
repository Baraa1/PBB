# Generated by Django 4.0 on 2023-11-15 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_customuser_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('color', models.CharField(blank=True, choices=[('Primary', 'Primary'), ('Info', 'Info'), ('Secondary', 'Secondary'), ('Light', 'Light'), ('Success', 'Success'), ('Danger', 'Danger'), ('Dark', 'Dark'), ('Warning', 'Warning')], default='Light', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('PR', 'Present'), ('AB', 'Absent'), ('SL', 'Sick Leave'), ('EM', 'Emergency Leave')], default='PR', max_length=100, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.shift')),
            ],
        ),
    ]
