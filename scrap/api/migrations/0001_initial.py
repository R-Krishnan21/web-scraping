# Generated by Django 3.0.7 on 2021-01-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('detail', models.TextField()),
                ('votes', models.IntegerField(default=0)),
                ('link', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('tags', models.CharField(max_length=200)),
            ],
        ),
    ]
