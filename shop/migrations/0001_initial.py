# Generated by Django 3.0.5 on 2020-05-04 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('superCategory', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Boys', 'Boys'), ('Girls', 'Girls'), ('Adult', 'Adult'), ('Children', 'Children'), ('All', 'All')], default='All', max_length=12)),
                ('subCategory', models.CharField(choices=[('Shirts', 'Shirts'), ('Pants', 'Pants'), ('Shoes', 'Shoes'), ('Accessories', 'Accessories'), ('Misc', 'Misc')], default='Misc', max_length=12)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sale', models.SmallIntegerField()),
                ('image', models.ImageField(default='missingItem.png', height_field=300, upload_to='items', width_field=300)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]