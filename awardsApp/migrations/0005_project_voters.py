# Generated by Django 3.0.8 on 2020-07-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsApp', '0004_auto_20200713_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='voters',
            field=models.ManyToManyField(related_name='voters', to='awardsApp.Profile'),
        ),
    ]
