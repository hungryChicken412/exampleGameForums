# Generated by Django 3.2.4 on 2021-10-03 16:45

import autoslug.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(default='', upload_to='blogThumbs/')),
                ('intro', models.TextField(max_length=200)),
                ('content', models.TextField()),
                ('published', models.DateTimeField(default=datetime.datetime(2021, 10, 3, 22, 15, 46, 523253))),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(default='', upload_to='blogThumbs/')),
                ('description', models.TextField(max_length=200)),
                ('price', models.IntegerField()),
                ('buy_url', models.URLField()),
            ],
        ),
    ]
