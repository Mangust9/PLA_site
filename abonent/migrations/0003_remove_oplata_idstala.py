# Generated by Django 2.0.2 on 2018-05-04 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abonent', '0002_auto_20180504_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oplata',
            name='idstala',
        ),
    ]
