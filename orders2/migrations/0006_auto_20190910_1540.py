# Generated by Django 2.1.5 on 2019-09-10 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders2', '0005_auto_20190910_1031'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='orderitem',
            index_together={('id',)},
        ),
    ]
