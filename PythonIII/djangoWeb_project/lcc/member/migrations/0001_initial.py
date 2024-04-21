# Generated by Django 4.2.7 on 2023-11-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=2)),
                ('birthday', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('c_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
