# Generated by Django 4.1.1 on 2023-06-27 17:29

from django.db import migrations, models

from dandiapi.api.models.asset import ASSET_COMPUTED_FIELDS


def remove_unpublished_asset_fields(apps, schema_editor):
    Asset = apps.get_model('api', 'Asset')
    Asset.objects.filter(published=False, metadata__has_any_keys=ASSET_COMPUTED_FIELDS).update(
        metadata=models.F('metadata') - ASSET_COMPUTED_FIELDS
    )


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0041_assetblob_download_count_and_more'),
    ]

    operations = [
        migrations.RunPython(remove_unpublished_asset_fields),
    ]
