# Generated by Django 4.2.7 on 2023-11-29 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_remove_home_socialmedia_links_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='Social_Name',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]