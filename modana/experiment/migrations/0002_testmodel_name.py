# Generated by Django 2.0 on 2018-06-14 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
