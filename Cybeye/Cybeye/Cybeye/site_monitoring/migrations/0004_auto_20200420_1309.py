# Generated by Django 3.0.5 on 2020-04-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_monitoring', '0003_auto_20200420_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
    ]
