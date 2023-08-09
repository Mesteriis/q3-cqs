# Generated by Django 4.2.3 on 2023-08-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_report_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('reviewed', 'Reviewed')], default='pending', max_length=20),
        ),
    ]