# Generated by Django 3.0.2 on 2020-01-13 04:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CotacaoModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('num_adultos', models.PositiveIntegerField(null=True)),
                ('num_criancas', models.PositiveIntegerField()),
                ('idade_crianca1', models.PositiveIntegerField(blank=True, null=True)),
                ('idade_crianca2', models.PositiveIntegerField(blank=True, null=True)),
                ('idade_crianca3', models.PositiveIntegerField(blank=True, null=True)),
                ('idade_crianca4', models.PositiveIntegerField(blank=True, null=True)),
                ('valor_cotacao', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-criado',),
            },
        ),
    ]
