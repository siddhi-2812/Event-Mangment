# Generated by Django 5.0 on 2024-02-09 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_gallery_rename_address_graduation_address_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='graduation',
        ),
    ]