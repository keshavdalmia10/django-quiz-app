# Generated by Django 3.0.3 on 2020-06-18 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20200617_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersanswer',
            name='quiz_taker',
        ),
    ]
