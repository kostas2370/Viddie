# Generated by Django 4.0.3 on 2023-11-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videomanagement', '0010_alter_videos_output'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='output',
            field=models.FileField(upload_to='media/output'),
        ),
    ]
