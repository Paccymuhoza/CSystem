# Generated by Django 2.2.5 on 2019-09-25 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20190924_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='college',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
