# Generated by Django 4.0 on 2022-01-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0023_embargoedzarrarchive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embargoedzarrarchive',
            name='file_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='embargoedzarrarchive',
            name='size',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='zarrarchive',
            name='file_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='zarrarchive',
            name='size',
            field=models.BigIntegerField(default=0),
        ),
    ]
