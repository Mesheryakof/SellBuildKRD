# Generated by Django 2.2 on 2021-07-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sell', '0014_auto_20210728_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='headerImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
