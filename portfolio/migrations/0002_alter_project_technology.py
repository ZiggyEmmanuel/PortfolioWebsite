# Generated by Django 4.2.7 on 2023-11-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Technology',
            field=models.CharField(max_length=50),
        ),
    ]
