# Generated by Django 2.2.7 on 2019-11-17 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20191116_1755'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bonds',
        ),
        migrations.DeleteModel(
            name='Cash',
        ),
        migrations.DeleteModel(
            name='HedgeFunds',
        ),
        migrations.DeleteModel(
            name='MutualFunds',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
