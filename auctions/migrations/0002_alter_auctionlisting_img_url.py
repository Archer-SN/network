# Generated by Django 4.0.4 on 2022-04-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='img_url',
            field=models.URLField(blank=True),
        ),
    ]
