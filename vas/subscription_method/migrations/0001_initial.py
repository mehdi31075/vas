# Generated by Django 2.0.7 on 2018-09-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30)),
                ('keyword', models.CharField(max_length=100)),
                ('channel', models.CharField(max_length=100)),
                ('fromKey', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=100)),
                ('NotificationId', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=100)),
            ],
        ),
    ]
