# Generated by Django 3.0.4 on 2020-04-04 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_two', '0002_remove_images_caption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='texts',
            old_name='metadata',
            new_name='keywords',
        ),
        migrations.AddField(
            model_name='texts',
            name='screenshots',
            field=models.IntegerField(default=0),
        ),
    ]
