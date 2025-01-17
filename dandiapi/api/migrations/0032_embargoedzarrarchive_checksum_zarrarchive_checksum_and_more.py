# Generated by Django 4.0.6 on 2022-07-07 21:36

from django.db import migrations, models


def forward_set_checksum(apps, schema_editor):
    ZarrArchive = apps.get_model('api', 'ZarrArchive')  # noqa: N806

    # Set any zarrs with a checksum of `None` (should be all) to have the status of `Pending`,
    # in order to satisfy model constraints.
    ZarrArchive.objects.filter(checksum__isnull=True).update(status='Pending')


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0031_asset_asset_metadata_has_schema_version_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='embargoedzarrarchive',
            name='checksum',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='zarrarchive',
            name='checksum',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
        # Mark zarrs with null checksums as pending, to satisfy below constraints
        migrations.RunPython(forward_set_checksum),
        migrations.AddConstraint(
            model_name='embargoedzarrarchive',
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(('checksum__isnull', True), ('status__in', ['Pending', 'Ingesting'])),
                    models.Q(('checksum__isnull', False), ('status', 'Complete')),
                    _connector='OR',
                ),
                name='consistent-embargo-checksum-status',
            ),
        ),
        migrations.AddConstraint(
            model_name='zarrarchive',
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(('checksum__isnull', True), ('status__in', ['Pending', 'Ingesting'])),
                    models.Q(('checksum__isnull', False), ('status', 'Complete')),
                    _connector='OR',
                ),
                name='consistent-checksum-status',
            ),
        ),
    ]
