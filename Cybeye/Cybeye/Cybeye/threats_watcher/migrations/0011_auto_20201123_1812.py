# Generated by Django 3.1.3 on 2020-11-23 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threats_watcher', '0010_auto_20201102_1151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bannedword',
            options={'verbose_name': 'block word', 'verbose_name_plural': 'Blocklist'},
        ),
    ]
