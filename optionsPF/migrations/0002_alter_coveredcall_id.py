# Generated by Django 3.2.4 on 2021-06-15 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('optionsPF', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coveredcall',
            name='id',
            field=models.OneToOneField(default=models.BigAutoField(primary_key=True), on_delete=django.db.models.deletion.SET_DEFAULT, primary_key=True, serialize=False, to='optionsPF.portfolio'),
        ),
    ]
