# Generated by Django 4.2.13 on 2024-07-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apepat', models.CharField(max_length=100)),
                ('apemat', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
            ],
        ),
    ]
