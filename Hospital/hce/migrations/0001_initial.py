# Generated by Django 5.1.2 on 2024-10-30 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Marca', models.TextField(max_length=100)),
                ('Modelo', models.TextField(max_length=100)),
                ('Serial', models.TextField(max_length=100)),
                ('Área', models.TextField(max_length=100)),
                ('Responsable', models.TextField(max_length=100)),
            ],
        ),
    ]