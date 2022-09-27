# Generated by Django 4.1.1 on 2022-09-27 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0004_favoritemovie_choose_favorite_later_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavoriteSerial',
            new_name='ActionsWithMovie',
        ),
        migrations.RenameModel(
            old_name='FavoriteMovie',
            new_name='ActionsWithSerial',
        ),
        migrations.AlterField(
            model_name='actionswithmovie',
            name='cinema_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.movie'),
        ),
        migrations.AlterField(
            model_name='actionswithserial',
            name='cinema_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.serial'),
        ),
    ]