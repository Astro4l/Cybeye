

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_leak', '0007_alert_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PastId',
            new_name='PasteId',
        ),
        migrations.RenameField(
            model_name='pasteid',
            old_name='past_id',
            new_name='paste_id',
        ),
    ]
