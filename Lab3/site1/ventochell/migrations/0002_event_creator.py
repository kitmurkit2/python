# Generated by Django 2.1.1 on 2018-09-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventochell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.CharField(default='Anonymous', max_length=15),
        ),
    ]