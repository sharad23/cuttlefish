# Generated by Django 2.0 on 2018-06-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autho', '0003_auto_20180612_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
