# Generated by Django 3.0.2 on 2020-01-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracao', '0003_configuracaotexto_padrao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracao',
            name='valor_final',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='configuracao',
            name='valor_inicial',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
