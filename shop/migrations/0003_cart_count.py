# Generated by Django 3.0.5 on 2020-05-05 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200504_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='count',
            field=models.SmallIntegerField(default=1),
        ),
    ]
