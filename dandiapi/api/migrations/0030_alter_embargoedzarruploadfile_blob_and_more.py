# Generated by Django 4.0.6 on 2022-07-10 20:54

from django.db import migrations, models

import dandiapi.api.storage


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0029_alter_usermetadata_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embargoedzarruploadfile',
            name='blob',
            field=models.FileField(
                blank=True,
                max_length=1000,
                storage=dandiapi.api.storage.get_embargo_storage,
                upload_to='',
            ),
        ),
        migrations.AlterField(
            model_name='zarruploadfile',
            name='blob',
            field=models.FileField(
                blank=True, max_length=1000, storage=dandiapi.api.storage.get_storage, upload_to=''
            ),
        ),
    ]
