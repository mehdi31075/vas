# Generated by Django 2.0.7 on 2018-09-13 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otpId', models.CharField(max_length=30)),
                ('statusId', models.CharField(max_length=100)),
                ('recipient', models.CharField(max_length=100)),
            ],
        ),
    ]
