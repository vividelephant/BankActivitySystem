# Generated by Django 3.1.5 on 2021-02-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_customer_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='group',
            field=models.CharField(default='', max_length=20, verbose_name='组'),
        ),
        migrations.AddField(
            model_name='customer',
            name='town',
            field=models.CharField(default='', max_length=20, verbose_name='镇子'),
        ),
        migrations.AddField(
            model_name='customer',
            name='village',
            field=models.CharField(default='', max_length=20, verbose_name='村子'),
        ),
    ]
