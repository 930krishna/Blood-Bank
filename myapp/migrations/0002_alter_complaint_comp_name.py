# Generated by Django 4.0.6 on 2022-08-31 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='comp_name',
            field=models.CharField(max_length=255),
        ),
    ]