# Generated by Django 4.1.1 on 2022-09-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(default='Russia', max_length=100),
        ),
        migrations.AlterField(
            model_name='serial',
            name='country',
            field=models.CharField(default='Russia', max_length=100),
        ),
    ]
