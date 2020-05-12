# Generated by Django 3.0.5 on 2020-05-12 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0004_auto_20200507_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nwbfile',
            name='subject',
        ),
        migrations.AddField(
            model_name='nwbfile',
            name='dandiset',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='nwb_files', to='publish.Dandiset'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
