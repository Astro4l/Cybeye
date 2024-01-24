

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('data_leak', '0002_data_leak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='url',
            field=models.URLField(default='', max_length=250),
        ),
    ]
