# Generated by Django 3.2.4 on 2021-06-15 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optionsPF', '0002_alter_coveredcall_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coveredcall',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
