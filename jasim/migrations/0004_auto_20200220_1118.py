# Generated by Django 3.0.3 on 2020-02-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jasim', '0003_auto_20200220_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='photos',
            field=models.ImageField(null=True, upload_to='screenshots'),
        ),
    ]