# Generated by Django 4.1.7 on 2023-03-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=20)),
                ('cpf_cliente', models.CharField(max_length=11)),
                ('endereço_cliente', models.CharField(max_length=100)),
                ('cidade_cliente', models.CharField(max_length=10)),
                ('estado_cliente', models.CharField(max_length=6)),
            ],
        ),
    ]