# Generated by Django 4.1.4 on 2023-01-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0034_services_order_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True, verbose_name='Name')),
                ('description', models.CharField(max_length=70, null=True, verbose_name='description')),
            ],
        ),
    ]
