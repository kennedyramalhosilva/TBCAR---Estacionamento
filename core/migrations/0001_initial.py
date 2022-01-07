# Generated by Django 3.1.7 on 2021-03-31 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('complemento', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=30)),
                ('foto', models.ImageField(upload_to='fotos_cliente')),
            ],
        ),
    ]