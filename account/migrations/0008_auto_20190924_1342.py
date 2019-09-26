# Generated by Django 2.2.5 on 2019-09-24 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190924_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college_council',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='department_council',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='school_council',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
