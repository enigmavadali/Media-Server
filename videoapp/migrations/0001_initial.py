# Generated by Django 2.1.4 on 2019-03-11 08:22

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(default='')),
                ('v_id', models.IntegerField(default=0)),
                ('body', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('docfile', models.FileField(upload_to='videos/admin/')),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('thumbnail', models.ImageField(default=0, upload_to='')),
                ('mpdfile', models.FileField(default=0, upload_to='')),
                ('tag', models.TextField(default='')),
                ('is_time_started', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(default='')),
                ('vid_id', models.IntegerField(default=0)),
                ('tag', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('docfile', models.FileField(upload_to='videos/professor/')),
                ('antim_tarikh', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('start_hour', models.IntegerField()),
                ('start_min', models.IntegerField()),
                ('end_hour', models.IntegerField()),
                ('end_min', models.IntegerField()),
                ('views', models.IntegerField(default=0)),
                ('thumbnail', models.ImageField(default=0, upload_to='')),
                ('tag', models.TextField(default='')),
                ('mpdfile', models.FileField(default=0, upload_to='')),
                ('is_time_started', models.BooleanField(default=False)),
                ('reg_students', django_mysql.models.ListCharField(models.CharField(max_length=50), default='', max_length=40800, size=800)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(null=True)),
                ('vid_id', models.IntegerField(default=0)),
                ('liked', models.BooleanField(default=False)),
            ],
        ),
    ]
