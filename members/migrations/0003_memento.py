# Generated by Django 4.1.7 on 2023-02-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
