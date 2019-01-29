# Generated by Django 2.0.5 on 2018-08-18 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_auto_20180809_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter_enabled', models.BooleanField(default=False)),
                ('counter_word', models.CharField(blank=True, max_length=50)),
                ('counter', models.IntegerField(blank=True)),
                ('timer_enabled', models.BooleanField(default=False)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('notes', models.CharField(max_length=200)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='goals.Task')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]