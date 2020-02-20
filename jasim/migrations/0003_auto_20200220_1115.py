# Generated by Django 3.0.3 on 2020-02-20 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jasim', '0002_auto_20200217_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='photos',
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(null=True, upload_to='media/screenshots')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='jasim.Project')),
            ],
        ),
    ]