# Generated by Django 4.1.1 on 2022-11-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_order_repair_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairstage',
            name='stage',
            field=models.CharField(max_length=40, verbose_name='Стадия ремонта'),
        ),
    ]