# Generated by Django 2.2.4 on 2019-09-07 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='описание')),
                ('img', models.CharField(max_length=128, verbose_name='img URL')),
            ],
        ),
    ]
