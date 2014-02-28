# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='title',
            field=models.CharField(max_length=20, default='Addition Interiors'),
            preserve_default=True,
        ),
    ]
