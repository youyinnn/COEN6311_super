# Generated by Django 3.2.9 on 2021-11-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_id', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('abstract', models.TextField()),
                ('venue', models.TextField()),
                ('year', models.IntegerField()),
                ('citations', models.IntegerField()),
                ('url', models.TextField()),
            ],
        ),
    ]