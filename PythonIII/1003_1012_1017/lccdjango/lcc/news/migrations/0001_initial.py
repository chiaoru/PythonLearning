# Generated by Django 4.2.5 on 2023-09-19 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('photo_url', models.CharField(max_length=200)),
                ('c_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
