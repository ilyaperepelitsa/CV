# Generated by Django 2.1.4 on 2018-12-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0007_tracker'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='positive_tracking',
            field=models.BooleanField(default=True),
        ),
    ]
