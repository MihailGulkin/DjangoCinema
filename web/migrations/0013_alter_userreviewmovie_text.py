# Generated by Django 4.1.1 on 2022-10-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_userreviewmovie_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreviewmovie',
            name='text',
            field=models.TextField(max_length=10000),
        ),
    ]