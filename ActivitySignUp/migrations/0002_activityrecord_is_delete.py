# Generated by Django 3.1.5 on 2021-02-01 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivitySignUp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityrecord',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否已删除'),
        ),
    ]