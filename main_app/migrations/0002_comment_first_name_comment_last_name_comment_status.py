# Generated by Django 4.2.2 on 2023-07-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='comment',
            name='last_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]