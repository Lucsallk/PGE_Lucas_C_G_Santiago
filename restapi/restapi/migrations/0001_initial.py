# Generated by Django 4.1.3 on 2022-11-15 06:20

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estagiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(max_length=220)),
                ('cpf', cpf_field.models.CPFField(max_length=11, unique=True)),
                ('dataNascimento', models.DateField()),
                ('cursoGrad', models.CharField(max_length=120)),
                ('instEnsino', models.CharField(max_length=220)),
                ('cargaHoraria', models.SmallIntegerField()),
                ('setorAlocado', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=220)),
                ('chefe', models.CharField(max_length=200)),
                ('capacidadeSetor', models.SmallIntegerField()),
            ],
        ),
    ]