# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0003_auto_20140228_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='slider_order',
            field=models.PositiveSmallIntegerField(blank=True, null=True, default=1),
            preserve_default=True,
        ),
    ]
