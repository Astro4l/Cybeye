

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_leak', '0004_auto_20200227_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
