# Generated by Django 4.0.6 on 2022-07-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistiteam',
            name='content',
            field=models.TextField(),
        ),
    ]