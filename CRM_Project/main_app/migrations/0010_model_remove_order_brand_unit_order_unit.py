# Generated by Django 4.1.1 on 2022-11-19 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_order_brand_alter_brand_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='brand',
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='unit', to='main_app.brand')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='unit', to='main_app.model')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order', to='main_app.unit'),
        ),
    ]
