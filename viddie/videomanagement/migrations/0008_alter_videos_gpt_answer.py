# Generated by Django 4.0.3 on 2023-11-04 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videomanagement', '0007_videos_gpt_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='gpt_answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
