# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-25 15:34


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Failover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disabled', models.BooleanField(default=False)),
                ('master', models.BooleanField(default=False)),
                ('timeout', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'system_failover',
                'verbose_name': 'Failover',
                'verbose_name_plural': 'Failovers',
            },
        ),
    ]
