# Generated by Django 2.0.2 on 2018-02-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180205_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='whisper',
            options={'get_latest_by': '-time_stamp'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='posts.Category'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, default='whisper_images/None/no-img.png', null=True, upload_to='whisper_images/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='whisper',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='posts.Category'),
        ),
        migrations.AlterField(
            model_name='whisper',
            name='image',
            field=models.ImageField(blank=True, default='whisper_images/None/no-img.png', null=True, upload_to='whisper_images/'),
        ),
        migrations.AlterField(
            model_name='whisper',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]
