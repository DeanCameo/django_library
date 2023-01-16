# Generated by Django 4.1.5 on 2023-01-15 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField(default=0)),
                ('book_name', models.CharField(default='none', max_length=30)),
                ('author_name', models.CharField(default='none', max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('book_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.IntegerField(default=0)),
                ('full_name', models.CharField(default='none', max_length=30)),
                ('address', models.CharField(default='none', max_length=50)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.IntegerField(default=0)),
                ('book_id', models.IntegerField(default=0)),
                ('loan_date', models.DateTimeField(verbose_name='date loan')),
                ('return_date', models.DateTimeField(verbose_name='date return')),
            ],
        ),
    ]
