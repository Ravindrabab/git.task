# Generated by Django 5.0 on 2023-12-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fristapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=100)),
                ('budget', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('heroname', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
