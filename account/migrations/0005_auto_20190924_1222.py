# Generated by Django 2.2.5 on 2019-09-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190924_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='member',
            name='reg_number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='staff_id',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
