# Generated by Django 4.2.5 on 2023-09-22 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to='files'),
        ),
    ]
