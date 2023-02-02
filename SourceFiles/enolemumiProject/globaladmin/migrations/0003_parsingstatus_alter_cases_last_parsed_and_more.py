# Generated by Django 4.1.5 on 2023-02-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globaladmin', '0002_cases_last_parsed'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParsingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='stopped', max_length=100)),
                ('last_parsed', models.CharField(default='02/02/2023, 08:36:16', max_length=100)),
                ('site', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='cases',
            name='last_parsed',
            field=models.CharField(default='02/02/2023, 08:36:16', max_length=150),
        ),
        migrations.AlterField(
            model_name='cases',
            name='site',
            field=models.CharField(max_length=300),
        ),
    ]
