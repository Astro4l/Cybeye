

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_leak', '0008_auto_20200403_1502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keyword',
            options={'ordering': ['name'], 'verbose_name_plural': 'Keywords Monitored'},
        ),
    ]
