# Generated by Django 4.1.4 on 2022-12-26 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0033_remove_order_type_of_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='services',
            field=models.ManyToManyField(to='main_app.services', verbose_name='Sevices'),
        ),
    ]
