# Generated by Django 4.1.5 on 2023-02-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_to_file', models.CharField(max_length=100)),
                ('classification', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=100)),
            ],
        ),
    ]