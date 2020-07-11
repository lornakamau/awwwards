# Generated by Django 3.0.8 on 2020-07-11 07:32

import cloudinary.models
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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('bio', models.TextField()),
                ('location', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('link', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('screenshot', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('design_score', models.IntegerField(default=0)),
                ('usability_score', models.IntegerField(default=0)),
                ('content_score', models.IntegerField(default=0)),
                ('average_design', models.FloatField(default=0)),
                ('average_usability', models.FloatField(default=0)),
                ('average_content', models.FloatField(default=0)),
                ('average_score', models.FloatField(default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awardsApp.Profile')),
                ('voters', models.ManyToManyField(related_name='votes', to='awardsApp.Profile')),
            ],
        ),
    ]
