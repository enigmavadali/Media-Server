# Generated by Django 2.1.4 on 2019-03-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='obj_type',
            field=models.CharField(default='', max_length=10),
        ),
    ]
