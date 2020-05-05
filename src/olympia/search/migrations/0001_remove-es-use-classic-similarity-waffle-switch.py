# Generated by Django 2.2.12 on 2020-05-05 13:39

from django.db import migrations


def remove_waffle_switch(apps, schema_editor):
    Switch = apps.get_model('waffle', 'Switch')
    Switch.objects.filter(name='es-use-classic-similarity').all().delete()


class Migration(migrations.Migration):
    dependencies = []
    operations = [migrations.RunPython(remove_waffle_switch)]
