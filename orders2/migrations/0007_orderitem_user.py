# Generated by Django 2.1.5 on 2019-09-11 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders2', '0006_auto_20190910_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orderitems', to=settings.AUTH_USER_MODEL),
        ),
    ]
