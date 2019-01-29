# Generated by Django 2.0.5 on 2018-08-07 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0003_auto_20180528_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=50)),
                ('goal_description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('values', models.ManyToManyField(to='goals.Value')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]