# Generated by Django 3.0.3 on 2020-06-15 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20200614_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='ans',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='ques',
            new_name='label',
        ),
        migrations.CreateModel(
            name='UsersAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
            ],
        ),
    ]
