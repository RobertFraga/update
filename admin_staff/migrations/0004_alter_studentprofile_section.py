# Generated by Django 4.2.16 on 2024-11-06 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0003_remove_studentprofile_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_staff.section'),
        ),
    ]
