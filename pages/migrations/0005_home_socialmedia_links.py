# Generated by Django 4.2.7 on 2023-11-29 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_services_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='SocialMedia_links',
            field=models.URLField(blank=True),
        ),
    ]
