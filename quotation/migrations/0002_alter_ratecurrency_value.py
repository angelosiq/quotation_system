# Generated by Django 3.2.9 on 2022-06-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratecurrency',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor'),
        ),
    ]
