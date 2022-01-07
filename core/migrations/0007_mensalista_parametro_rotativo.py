# Generated by Django 3.1.7 on 2021-05-06 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210331_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Parâmetros',
            },
        ),
        migrations.CreateModel(
            name='Rotativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateTimeField()),
                ('data_saida', models.DateTimeField(blank=True, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pago', models.BooleanField(default=False)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('id_parametro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.parametro')),
                ('id_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.veiculo')),
            ],
            options={
                'verbose_name_plural': 'Rotativos',
            },
        ),
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('id_parametro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.parametro')),
                ('id_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.veiculo')),
            ],
            options={
                'verbose_name_plural': 'Mensalistas',
            },
        ),
    ]
