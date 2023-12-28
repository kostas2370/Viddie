# Generated by Django 4.0.3 on 2023-11-21 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videomanagement', '0016_backgrounds_image_resize_horizontal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatars',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='backgrounds',
            name='image_resize_horizontal',
        ),
        migrations.RemoveField(
            model_name='backgrounds',
            name='image_resize_vertical',
        ),
        migrations.AlterField(
            model_name='avatars',
            name='file',
            field=models.FileField(upload_to='media/other/avatar'),
        ),
        migrations.AlterField(
            model_name='avatars',
            name='voice',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='videomanagement.voicemodels'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='backgrounds',
            name='avatar_pos_left',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='backgrounds',
            name='avatar_pos_top',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='backgrounds',
            name='image_pos_left',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='backgrounds',
            name='image_pos_top',
            field=models.IntegerField(),
        ),
    ]
