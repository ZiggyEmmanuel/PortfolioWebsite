# Generated by Django 4.2.7 on 2023-11-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='Career',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='home',
            name='Greetings',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='home',
            name='Name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='services',
            name='Service_Name',
            field=models.CharField(max_length=40),
        ),
    ]
