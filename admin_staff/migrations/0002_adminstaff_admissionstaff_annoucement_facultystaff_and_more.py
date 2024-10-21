# Generated by Django 4.2.16 on 2024-10-21 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminStaff',
            fields=[
                ('admin_staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(blank=True, max_length=24, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'admin_staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AdmissionStaff',
            fields=[
                ('admission_staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(blank=True, max_length=24, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'admission_staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Annoucement',
            fields=[
                ('annoucement_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
            ],
            options={
                'db_table': 'annoucement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FacultyStaff',
            fields=[
                ('faculty_staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(blank=True, max_length=24, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'faculty_staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GuidanceStaff',
            fields=[
                ('guidance_staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(blank=True, max_length=24, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'guidance_staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegistrarStaff',
            fields=[
                ('registrar_staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(blank=True, max_length=24, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'registrar_staff',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='studentprofile',
            options={'managed': True},
        ),
    ]