# Generated by Django 3.0.2 on 2020-01-13 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracaotexto',
            name='padrao',
        ),
    ]
