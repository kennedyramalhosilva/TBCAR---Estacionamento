# Generated by Django 3.1.7 on 2021-03-31 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('ano', models.CharField(max_length=20)),
                ('cor', models.CharField(max_length=30)),
                ('placa', models.CharField(max_length=10)),
                ('foto', models.ImageField(upload_to='fotos_veiculos')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
    ]