# Generated by Django 3.2.4 on 2021-06-23 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('optionsPF', '0003_auto_20210623_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='user',
            field=models.OneToOneField(default='8', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
