# Generated by Django 2.2.8 on 2020-01-09 16:33

import backend.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OldManInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30, null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('medical_history', models.CharField(max_length=30, null=True)),
                ('allergy', models.CharField(max_length=30, null=True)),
                ('blood_type', models.CharField(max_length=10, null=True)),
                ('drugs', models.CharField(max_length=30, null=True)),
                ('treatment', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QrCode',
            fields=[
                ('qr_code_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('old_man_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='backend.OldManInfo')),
            ],
            bases=(models.Model, backend.models.PhoneNumberMethod),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=50)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]
