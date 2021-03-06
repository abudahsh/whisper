# Generated by Django 2.0.2 on 2018-02-04 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('likes', models.PositiveSmallIntegerField(default=0)),
                ('comments', models.PositiveSmallIntegerField(default=0)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='posts.Category')),
            ],
            options={
                'ordering': ['-time_stamp'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Whisper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('likes', models.PositiveSmallIntegerField(default=0)),
                ('comments', models.PositiveSmallIntegerField(default=0)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='posts.Category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whisper', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'time_stamp',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Whisper'),
        ),
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
