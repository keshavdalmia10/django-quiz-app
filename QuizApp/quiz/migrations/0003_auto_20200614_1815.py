# Generated by Django 3.0.3 on 2020-06-14 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option4',
        ),
    ]
