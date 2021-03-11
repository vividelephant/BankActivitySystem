# Generated by Django 3.1.5 on 2021-02-01 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSecond', '0001_initial'),
        ('AdminThird', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminthird',
            name='admin_second',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AdminSecond.adminsecond', verbose_name='二级管理员'),
        ),
    ]