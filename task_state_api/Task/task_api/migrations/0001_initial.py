# Generated by Django 3.0.14 on 2021-12-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Task',
                'db_table': 'Task',
            },
        ),
    ]
