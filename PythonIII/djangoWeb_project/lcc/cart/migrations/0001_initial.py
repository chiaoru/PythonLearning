# Generated by Django 4.2.7 on 2023-11-30 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.IntegerField(default=0)),
                ('shipping', models.IntegerField(default=0)),
                ('grandtotal', models.IntegerField(default=0)),
                ('customename', models.CharField(max_length=50)),
                ('customeemail', models.CharField(max_length=100)),
                ('customephone', models.CharField(max_length=20)),
                ('customeaddress', models.CharField(max_length=200)),
                ('paytype', models.CharField(max_length=10)),
                ('bankaccount', models.CharField(max_length=10, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('unitprice', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('dtotal', models.IntegerField(default=0)),
                ('dorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.ordermodel')),
            ],
        ),
    ]
