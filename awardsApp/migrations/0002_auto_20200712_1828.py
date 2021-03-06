# Generated by Django 3.0.8 on 2020-07-12 18:28

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awardsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-post_date']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Project screenshot'),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('design', models.IntegerField(default=0)),
                ('usability', models.IntegerField(default=0)),
                ('content', models.IntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='awardsApp.Project')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awardsApp.Profile')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]
